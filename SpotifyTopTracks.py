import os
import spotipy
import spotipy.util as util
import requests
import numpy as np
os.environ["SPOTIPY_CLIENT_ID"] = "CLIENT_ID_HERE"
os.environ["SPOTIPY_CLIENT_SECRET"] = "CLIENT_SECRET_HERE"
os.environ["SPOTIPY_REDIRECT_URI"] = "http://localhost:8080"
username = "melroy_caeiro"
scope = "user-read-playback-state user-read-currently-playing user-top-read"
uri = "http://localhost:8080"
currentTrack = 1000
x = 1
token = util.prompt_for_user_token(username, scope, os.environ["SPOTIPY_CLIENT_ID"], os.environ["SPOTIPY_CLIENT_SECRET"], uri)
sp = spotipy.Spotify(auth=token)

playback = sp.current_playback()
nowPlaying = sp.current_user_playing_track()
top = sp.current_user_top_tracks(limit=20, time_range="long_term")

nTrackName = []
nTrackArtists = []

i = 0
while i < 20:
    nTrackName.append(top["items"][i]["name"])
    nTrackArtists.append(top["items"][i]["artists"][0]["name"])
    print(nTrackName[i] + " by " + nTrackArtists[i].upper())
    i = i+1
