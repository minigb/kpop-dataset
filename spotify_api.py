import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import pandas as pd
from omegaconf import OmegaConf

# Load the Spotify API credentials
spotify_conf = OmegaConf.load('spotify_keys.yaml')
client_id = spotify_conf.client_id
client_secret = spotify_conf.client_secret

# Authenticate with Spotify
auth_manager = SpotifyClientCredentials(client_id=client_id, client_secret=client_secret)
sp = spotipy.Spotify(auth_manager=auth_manager)

def get_artist_id(artist_name):
    result = sp.search(q=artist_name, type='artist')
    artist_id = result['artists']['items'][0]['id']
    return artist_id

def get_all_songs(artist_id):
    songs = []
    albums = sp.artist_albums(artist_id, album_type='album,single')
    for album in albums['items']:
        album_id = album['id']
        album_tracks = sp.album_tracks(album_id)
        for track in album_tracks['items']:
            songs.append(track['name'])
    return songs

def save_to_csv(songs, artist_name):
    df = pd.DataFrame(songs, columns=['Song Title'])
    df.to_csv(f'{artist_name}_songs.csv', index=False)

def main(artist_name):
    artist_id = get_artist_id(artist_name)
    songs = get_all_songs(artist_id)
    save_to_csv(songs, artist_name)
    print(f"Saved {len(songs)} songs to {artist_name}_songs.csv")

if __name__ == '__main__':
    artist_name = input("Enter the artist name: ")
    main(artist_name)
