from django.shortcuts import render
from django.http import HttpResponse
from django.views import generic

from .models import BankImage
    
def remove_prefix(string):
    return "/".join(string.split("/")[2:])
    #return string.lstrip("/")


def index(request):
    images = BankImage.objects.all()

    context = { 'images': images }
    return render(request, 'image_bank/index.html', context)

def path_search(request):
    return render(request, 'image_bank/path_search.html')

def name_search(request):
    images = BankImage.objects.filter(path__icontains=request.GET.get('q'))
    context = { 'images': images }
    return render(request, 'image_bank/name_search.html', context)

def show_image(request):

    im_path = remove_prefix(request.path_info)
    metadata = BankImage.objects.filter(path=im_path)[0].metadata

    context = {
            'im_path' : remove_prefix(request.path_info),
            'metadata': metadata }
    #print(remove_prefix(request.path_info))
    
    return render(request, 'image_bank/show_image.html', context)
