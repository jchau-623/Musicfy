from .db import db
from .playlist_songs import playlist_songs

class Song(db.Model):
    __tablename__ = 'songs'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(50), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    artist_id = db.Column(db.Integer, db.ForeignKey('artists.id'), nullable=False)
    album_id = db.Column(db.Integer, db.ForeignKey('albums.id'))
    song_url = db.Column(db.String(500), nullable=False)
    image_url = db.Column(db.String(500))
    track_number = db.Column(db.Integer)

    user = db.relationship('User', back_populates='songs')
    artist = db.relationship('Artist', back_populates='songs')
    album = db.relationship('Album', back_populates='songs')
    playlists = db.relationship('Playlist', back_populates='songs', secondary=playlist_songs)

    def a_to_dict(self):
        return {
            'id': self.id,
            'title': self.title,
            'user': self.user.s_to_dict(),
            'artist': self.artist.to_dict(),
            'album': self.album.s_to_dict() if self.album else None,
            'song_url': self.song_url,
            'image_url': self.image_url,
            'track_number': self.track_number
        }

    def to_dict(self):
        return {
            'id': self.id,
            'title': self.title,
            'user': self.user.s_to_dict(),
            'artist': self.artist.to_dict(),
            'album': self.album.s_to_dict() if self.album else None,
            'song_url': self.song_url,
            'image_url': self.image_url,
            'track_number': self.track_number
        }

