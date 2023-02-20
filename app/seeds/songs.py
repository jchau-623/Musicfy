from app.models import db, Song

songs = [
     Song( #1
        title='Long Walk, Short Dock',
        user_id=1,
        artist_id=1,
        song_url='https://musicfy-bucket.s3.amazonaws.com/song-seeds/01+Long+Walk%2C+Short+Dock+(ft+Dillan+Witherow).mp3',
        image_url='https://cofi-bucket.s3.amazonaws.com/art-seeds/afterhours-art.png',
        track_number=1,
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
