from .db import db
from .playlist_songs import playlist_songs

class Playlist(db.Model):
    __tablename__ = 'playlists'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(50), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))

    user = db.relationship('User', back_populates='playlists')
    songs = db.relationship('Song', back_populates='playlists', secondary=playlist_songs)

    def to_dict(self):
        return {
            'id': self.id,
            'title': self.title,
            'songs': [song.a_to_dict() for song in self.songs],
            'song_ids': [song.id for song in self.songs],
        }
