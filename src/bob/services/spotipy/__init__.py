import os

from spotipy import Spotify, util


class Spotipy:
    scopes = [
        'user-library-read',
        'user-modify-playback-state',
        'user-read-playback-state',
        'streaming',
        'playlist-read-private',
    ]
    token = None
    sp = None

    def __init__(self):
        self.token = util.prompt_for_user_token(
            os.getenv('SPOTIFY_EMAIL'),
            ' '.join(self.scopes)
        )
        self.sp = Spotify(auth=self.token)
        # TODO: Check token, environment variables

    def search_and_play_track(self, title, device):
        results = self.sp.search(title, limit=1, offset=0, type='track',
                                 market="FR")
        uri = results.get('tracks').get('items')[0].get('uri')
        self.sp.start_playback(device.get('id'), uris=[uri])
