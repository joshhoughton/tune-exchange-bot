import configparser
import os
from typing import List

import spotipy
from fbchat import Client
from spotipy.oauth2 import SpotifyOAuth


PROJECT_PATH = os.path.dirname(__file__)


config = configparser.ConfigParser()
config.read(os.path.join(PROJECT_PATH, "config", "config.ini"))

spotify = spotipy.Spotify(auth_manager=SpotifyOAuth(
    username=config['spotify']['username'],
    scope=config['spotify']['scope'],
    client_id=config['spotify']['client_id'],
    client_secret=config['spotify']['client_secret'],
    redirect_uri=config['spotify']['redirect_uri'],
    open_browser=False,
))


def get_already_added_tracks(playlist_id: str) -> List[str]:
    """Get a list of track IDs that already exist in playlist `playlist_id`.

    Parameters
    ----------
    playlist_id : str
        desired playlist ID

    Returns
    -------
    List[str]
        list of Spotify track IDs
    """
    track_ids = []
    offset = 0

    while True:
        results = [
            row['track']['id']
            for row in spotify.playlist_tracks(
                playlist_id,
                fields="items(track(id))",
                limit=100,
                offset=offset
            )['items']
        ]

        if results:
            track_ids.extend(results)
            offset += len(results)
        else:
            break

    return track_ids


ALREADY_IN_PLAYLIST = get_already_added_tracks(config['spotify']['playlist'])

facebook = Client(config['facebook']['email'], config['facebook']['pass'])
