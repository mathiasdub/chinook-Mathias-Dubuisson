from django.shortcuts import render, get_object_or_404

from .models import Album

    
def index(request):
    query = request.GET.get('recherche', '')
    if query:
        albums = Album.objects.filter(title__icontains=query)
    else:
        albums = Album.objects.all()
    return render(request, 'disks/index.html', {'albums': albums, 'query': query})


def detail(request, album_id):
    album = get_object_or_404(Album, id=album_id)
    return render(request, 'disks/detail.html', {'album': album})