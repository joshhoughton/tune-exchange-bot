import configparser
import os

import spotipy
from fbchat import Client
from spotipy.oauth2 import SpotifyOAuth

from tune_exchange_bot.utils.spotify import get_already_added_tracks


PROJECT_PATH = os.path.dirname(__file__)


config = configparser.ConfigParser()
config.read(os.path.join(PROJECT_PATH, "config", "config.ini"))

spotify = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        username=config["spotify"]["username"],
        scope=config["spotify"]["scope"],
        client_id=config["spotify"]["client_id"],
        client_secret=config["spotify"]["client_secret"],
        redirect_uri=config["spotify"]["redirect_uri"],
        open_browser=False,
    )
)


ALREADY_IN_PLAYLIST = get_already_added_tracks(spotify, config["spotify"]["playlist"])

facebook = Client(config["facebook"]["email"], config["facebook"]["pass"])
