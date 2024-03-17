from django.urls import path
from galleryimg import views

urlpatterns = [
    path('', views.gallery_list, name="gallery_list")
]