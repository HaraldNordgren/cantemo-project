from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    #url('path_search', views.path_search, name='pathsearch'),
    #url(r'name_search', views.name_search, name='namesearch'),
    url('stored-images', views.show_image, name='imageshow')
]
