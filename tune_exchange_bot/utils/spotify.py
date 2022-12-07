from typing import List, Union

from tune_exchange_bot import config, spotify


PLAYLIST_ID = config["spotify"]["playlist"]


def add_to_playlist(track_id: Union[str, List[str]]):
    """_summary_

    Args:
        track_id (str): _description_
    """
    if type(track_id) is str:
        track_id = [track_id]

    spotify.playlist_add_items(PLAYLIST_ID, track_id)
