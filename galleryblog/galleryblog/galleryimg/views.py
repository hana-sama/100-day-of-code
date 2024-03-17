from django.shortcuts import render
from django.http import HttpResponse
from .models import Gallery
# Create your views here.
def gallery_list(request):
    # return HttpResponse("Are we on the right track?")
    gallery_objects = Gallery.objects.all()
    return render(request, 'gallery/gallery.html', {'gallery_objects': gallery_objects})