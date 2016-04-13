from django.shortcuts import render
from django.http import HttpResponse
from django.views import generic

from .models import BankImage
from .constants import *

import os

def remove_prefix(string):
    return "/".join(string.split("/")[3:])

def index(request):

    name_search = ""
    metadata_search = ""

    if request.GET.get('name_search'):
        name_search = request.GET.get('name_search')
        images = BankImage.objects.filter(path__icontains=name_search)
    elif request.GET.get('metadata_search'):
        metadata_search = request.GET.get('metadata_search')
        images = BankImage.objects.filter(metadata__icontains=metadata_search)
    elif request.POST.get('delete'):
        BankImage.objects.get(path=request.POST.get('short_path')).delete()
        os.remove("image_bank/" + request.POST.get('full_path'))
        images = BankImage.objects.all()
    else:
        images = BankImage.objects.all()

    image_data = []
    for im in images:
        short_path = im.path
        full_path = stored_images + im.path
        image_data.append( (short_path, full_path, im.metadata) )

    context = {
            'images': image_data,
            'name_search': name_search,
            'metadata_search': metadata_search}
    return render(request, 'image_bank/index.html', context)

def show_image(request):

    short_path = remove_prefix(request.path_info)
    full_path = watched_folder + short_path
    
    im = BankImage.objects.get(path=short_path)
    file_category = im.file_type.split("/")[0]

    if request.POST.get('metadata'):
        metadata = request.POST.get('metadata')
        im.metadata = metadata
        im.save()
    #elif request.POST:
    #    print(request.POST)
    #    metadata = ""
    else:
        metadata = BankImage.objects.get(path=short_path).metadata
    
    context = {
            'short_path'    : short_path,
            'full_path'     : full_path,
            'metadata'      : metadata,
            'file_category' : file_category,
            'file_type'     : im.file_type}

    return render(request, 'image_bank/show_image.html', context)
