from app.models import db, Song

songs = [
     Song( #1
        title='Long Walk, Short Dock',
        user_id=1,
        artist_id=1,
        song_url='',
        image_url='',
        album_id=1
    ),
]

def seed_songs():
    for song in songs:
        db.session.add(song)



    db.session.commit()


def undo_songs():
    db.session.execute('TRUNCATE songs RESTART IDENTITY CASCADE;')
    db.session.commit()
