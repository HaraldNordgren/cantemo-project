from django.shortcuts import render
from django.http import HttpResponse
from django.views import generic

from .models import BankImage
from .constants import *

"""
def path_search(request):
    return render(request, 'image_bank/path_search.html')

def name_search(request):
    images = BankImage.objects.filter(path__icontains=request.GET.get('q'))
    context = { 'images': images }
    return render(request, 'image_bank/name_search.html', context)
"""
    
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

    if request.method == 'POST':
        im = BankImage.objects.get(path=short_path)
        metadata = request.POST['metadata']
        im.metadata = metadata
        im.save()
    else:
        metadata = BankImage.objects.get(path=short_path).metadata
    
    context = {
            'im_path' : full_path,
            'metadata': metadata }

    return render(request, 'image_bank/show_image.html', context)
