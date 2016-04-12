from django.shortcuts import render
from django.http import HttpResponse
#from django.template import loader
from django.views import generic

from .models import BankImage
    
def remove_prefix(string):
    return "/".join(string.split("/")[2:])
    #return string.lstrip("/")


"""
class IndexView(generic.ListView):
    template_name = 'image_bank/index.html'
    context_object_name = 'images'

    def get_queryset(self):
        return BankImage.objects.all()
"""

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
    #im = BankImage.objects.filter(path=event.src_path)
    #print(remove_prefix(request.path_info))

    context = { 'im_path' : remove_prefix(request.path_info) }
    
    return render(request, 'image_bank/show_image.html', context)
