from bob.services.spotipy import Spotipy
from unittest.mock import patch


@patch(target='spotipy.util.prompt_for_user_token')
def test_init(prompt_for_user_token):
    prompt_for_user_token.return_value = 'fake_token'

    sp = Spotipy()

    assert sp.sp is not None


@patch(target='spotipy.client.Spotify.start_playback')
@patch(target='spotipy.client.Spotify.search')
@patch(target='spotipy.util.prompt_for_user_token')
def test_search_and_play_track(prompt_for_user_token, search, start_playback):
    prompt_for_user_token.return_value = 'fake_token'
    search.return_value = {'tracks': {'items': [{'uri': 'fake_uri'}]}}

    sp = Spotipy()
    sp.search_and_play_track('fake_title', {'id': 'fake_id'})

    search.assert_called_with('fake_title', limit=1, offset=0, type='track',
                                 market="FR")
    start_playback.assert_called_with('fake_id', uris=['fake_uri'])
