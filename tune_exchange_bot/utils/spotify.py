from typing import List, Union

from spotipy import Spotify


def add_to_playlist(spotify: Spotify, track_id: Union[str, List[str]], playlist: str):
    """Add a set of Spotify tracks to a playlist.

    Parameters
    ----------
    spotify : spotipy.Spotify
        authenticated Spotify object
    track_id : str or list of strs
        either a single or multiple Spotify track ids
    playlist : str
        Spotify playlist ID
    """
    if type(track_id) is str:
        track_id = [track_id]

    spotify.playlist_add_items(playlist, track_id)


def get_already_added_tracks(spotify: Spotify, playlist_id: str) -> List[str]:
    """Get a list of track IDs that already exist in playlist `playlist_id`.

    Parameters
    ----------
    spotify : spotipy.Spotify
        authenticated Spotify object
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
            row["track"]["id"]
            for row in spotify.playlist_tracks(
                playlist_id, fields="items(track(id))", limit=100, offset=offset
            )["items"]
        ]

        if results:
            track_ids.extend(results)
            offset += len(results)
        else:
            break

    return track_ids
