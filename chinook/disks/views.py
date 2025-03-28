from django.shortcuts import render, get_object_or_404

from .models import Album


def index(request):
    albums = Album.objects.all()
    return render(request, 'disks/index.html', {'albums': albums})