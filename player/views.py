from django.shortcuts import render

from .utils import name_list, tracks_list
from .forms import ArtistForm


import random


def home(request):
    if request.method == 'GET':
        form = ArtistForm(request.GET)
        if form.is_valid():
            rand_num = random.randint(0,21)
            rand_img = f"img/{rand_num}.jpg"
            cd = form.cleaned_data
            return render(request,'index.html',
                  {'artist_names':name_list(),
                   'tracks_list':tracks_list(int(cd['artist_name'])),
                   'rand_img':rand_img,
                   'form':form})
    form = ArtistForm()
    rand_num = random.randint(0,21)
    rand_img = f"img/{rand_num}.jpg"
    
    return render(request,'index.html',
                  {'artist_names':name_list(),
                   'tracks_list':tracks_list(0),
                   'rand_img':rand_img,
                   'form':form})
