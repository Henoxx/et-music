import json
from django.core.files.storage import default_storage


fh = default_storage.open('artist_data.json').read()
data = json.loads(fh)
def name_list():
    artist_names = []
    for artist in data:
        artist_names.append(artist["artist"])

    return artist_names

def tracks_list(i):
    tracks_list_data = data[i]["tracks"]

    return tracks_list_data

def id_name_tuple():
    touple_list = []
    pk = 0
    for artist in data:
        touple_form = (pk, artist["artist"])
        touple_list.append(touple_form)
        pk += 1

    return touple_list
