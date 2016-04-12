from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url('stored-images', views.show_image, name='imageshow')
]
