from django.shortcuts import render
from django.http import HttpResponse
from django.views import generic

from .models import BankImage
from .constants import *
    
def remove_prefix(string):
    return "/".join(string.split("/")[3:])
    #return string.lstrip("/")

def index(request):

    if request.GET.get('namesearch'):
        search = request.GET.get('namesearch')
        images = BankImage.objects.filter(path__icontains=search)
        #searched = True
    else:
        search = ""
        images = BankImage.objects.all()
        #searched = False

    paths = []
    for im in images:
        short_path = im.path
        full_path = stored_images + im.path
        paths.append( (short_path, full_path) )

    context = {
            'images': paths,
            'search': search}
    return render(request, 'image_bank/index.html', context)

def path_search(request):
    return render(request, 'image_bank/path_search.html')

def name_search(request):
    images = BankImage.objects.filter(path__icontains=request.GET.get('q'))
    context = { 'images': images }
    return render(request, 'image_bank/name_search.html', context)

def show_image(request):

    #print(request.path_info)
    short_path = remove_prefix(request.path_info)
    print("    " + short_path)
    metadata = BankImage.objects.filter(path=short_path)[0].metadata
    full_path = watched_folder + short_path

    context = {
            'im_path' : full_path,
            'metadata': metadata }
    #print(remove_prefix(request.path_info))
    
    return render(request, 'image_bank/show_image.html', context)
