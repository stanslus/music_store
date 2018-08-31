from django.shortcuts import render
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
