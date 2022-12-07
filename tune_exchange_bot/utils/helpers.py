import re


def parse_spotify_track_id(spotify_url: str) -> str:
    """Parse a Spotify track ID from a track URL.

    Args:
        spotify_url (str): a Spotify track URL

    Returns:
        str: a Spotify track ID
    """
    pattern = r".*(https?://)?open\.spotify\.com/track/([A-z0-9]{22}).*"

    match = re.match(pattern, spotify_url)

    if match:
        return match.group(2)
    else:
        return None
