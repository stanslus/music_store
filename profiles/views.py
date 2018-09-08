from django.shortcuts import render,redirect
from profiles.models import Album,Song
# Create your views here.
def home(request):
    context={}
    template='home.html'
    return render(request,template,context)
def index(request):
    context={}
    template='index.html'
    return render(request,template,context)
def about(request):
    context={}
    template="about.html"
    return render(request,template,context)
def song(request):
    #context={}
    template="song.html"
    songs= Song.objects.all()
    album = Album.objects.all()
    return render(request,template,{'song':songs,'album':album})
    #album and song variables are to be used in html file to fetch album and song data
def newAlbum(request):
    #context={}
    template="new.album.html"
    return render(request,template)
#function to obtain values from the form
def addAlbum(request):
    artist=request.GET['artist']
    albumName=request.GET['album_title']
    genre=request.GET['genre']
    album_logo=request.GET['album_logo']
#create an instance of module Album class
    newAlbum = Album.objects.create(
        artist=artist,
        album_title=albumName,
        genre=genre,
        album_logo=album_logo
    )
#save the object/instance
    newAlbum.save()
    return redirect('addAlbum')

def newSong(request):
    #context={}
    template="new.song.html"
    return render(request,template)
#function to obtain values from the form
def addSong(request):
    title=request.GET['song_title']
    fileType=request.GET['file_type']

#create an instance of module Album class
    newSong = Song.objects.create(
        song_title=title,
        file_type=fileType,
    )
#save the object/instance
    newSong.save()
    return redirect('addSong')

   