import pytest

from tune_exchange_bot.utils.helpers import parse_spotify_track_id


@pytest.mark.parametrize(
    'track_url,expected_id',
    [
        ("https://open.spotify.com/track/3WYVYoA0Usk0trYlSrGQWR", "3WYVYoA0Usk0trYlSrGQWR"),
        ("https://open.spotify.com/track/3WYVYoA0Usk0trYlSrGQWR?si=GalDkrGDQj6_uBJV9B3Tww", "3WYVYoA0Usk0trYlSrGQWR"),
        ("", None)
    ]
)
def test_parse_spotify_track_id(track_url: str, expected_id: str):
    """Test parse_spotify_track_id."""
    assert parse_spotify_track_id(track_url) == expected_id
