from .db import db
from datetime import datetime

class Album(db.Model):
    __tablename__ = 'albums'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(50), nullable=False)
    artist_id = db.Column(db.Integer, db.ForeignKey('artists.id'))
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    image_url = db.Column(db.String(500))

    user = db.relationship('User', back_populates='albums')
    artist = db.relationship('Artist', back_populates='albums')
    songs = db.relationship('Song', back_populates='album', cascade='all, delete-orphan')

    # for songs
    def s_to_dict(self):
        return {
            'id': self.id,
            'title': self.title,
            'artist': self.artist.to_dict(),
            'image_url': self.image_url
        }

    # for user
    def u_to_dict(self):
        return {
            'id': self.id,
            'title': self.title
        }

    def to_dict(self):
        return {
            'id': self.id,
            'title': self.title,
            'artist': self.artist.to_dict(),
            'image_url': self.image_url,
            'user': self.user.s_to_dict(),
            'songs': [song.a_to_dict() for song in self.songs],
        }
