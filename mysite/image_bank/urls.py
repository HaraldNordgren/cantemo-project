from django.conf.urls import url

from . import views

#app_name = "image_bank"

urlpatterns = [
    url(r'^$', views.index, name='index'),
    #url(r'^$', views.IndexView.as_view(), name='index'),
    url('path_search', views.path_search, name='pathsearch'),
    url(r'name_search', views.name_search, name='namesearch'),
    url('stored-images', views.show_image, name='imageshow')
]
