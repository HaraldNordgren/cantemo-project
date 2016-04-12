from django.shortcuts import render
from django.http import HttpResponse
#from django.template import loader

from .models import BankImage

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
