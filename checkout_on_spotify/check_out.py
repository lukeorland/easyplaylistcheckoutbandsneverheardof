import fileinput
from pyspotify import get_session

PLAYLIST_NAME = 'check out'


def get_or_create_playlist(session, title):
    playlist = session.playlist_container.get_or_create(PLAYLIST_NAME)
    if not playlist:
        playlist = session.create_playlist(title)
    return playlist


def process(session, artist):
    # find the band
    search = session.search('massive attack')
    search.load()
    found_artist = search.artists[0].load()
    # find the top 5 tracks for the band
    tracks = found_artist.tophit_tracks
    # add them to the playlist if they are not there already.
    playlist = get_or_create_playlist(session, PLAYLIST_NAME)
    playlist.add_tracks(tracks)


if __name__ == __main__:
    session = get_session()
    for line in fileinput.input():
        process(session, line)
