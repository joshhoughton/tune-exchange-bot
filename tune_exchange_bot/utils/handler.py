from tune_exchange_bot import ALREADY_IN_PLAYLIST, config, spotify
from tune_exchange_bot.utils.helpers import parse_spotify_track_id
from tune_exchange_bot.utils.logger import logger
from tune_exchange_bot.utils.spotify import add_to_playlist


def process_message(message_object: dict):
    """Process a fbchat message object.

    Args:
        message_object: a fb chat message object
    """
    message = message_object.text

    if not message:
        return

    track_id = parse_spotify_track_id(message_object.text)

    if track_id in ALREADY_IN_PLAYLIST:
        logger.warning(f"Track `{track_id}` is already in playlist, not adding.")
        return

    if track_id:
        logger.info(f"Adding `{track_id}` to playlist...")
        add_to_playlist(spotify, track_id, playlist=config["spotify"]["playlist"])
        ALREADY_IN_PLAYLIST.append(track_id)
    else:
        logger.debug(f"Message `{message}` did not contain a track ID.")
