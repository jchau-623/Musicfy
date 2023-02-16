from app.models import db, Song

songs = [
    Song(

    )
]

def seed_songs():
    for song in songs:
        db.session.add(song)



    db.session.commit()


def undo_songs():
    db.session.execute('TRUNCATE songs RESTART IDENTITY CASCADE;')
    db.session.commit()
