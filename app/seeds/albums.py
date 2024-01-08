from app.models import db, Album
from app.seeds.songs import songs
from app.seeds.album_likes import add_likes_to_albums

albums = [
    Album( #1
        title='Beyond The Veil(Deluxe)',
        artist_id=1,
        user_id=1,
        image_url='https://yuhtube-bucket.s3.amazonaws.com/album-seeds/beyondtheveil-album.jpg'
    ),
    Album( #2
        title='Ashes',
        artist_id=2,
        user_id=1,
        image_url='https://yuhtube-bucket.s3.amazonaws.com/album-seeds/ashes-album.jpg'
    ),
    Album( #3
        title='Anomaly',
        artist_id=3,
        user_id=1,
        image_url='https://yuhtube-bucket.s3.amazonaws.com/album-seeds/anomaly-album.jpg'
    ),
    Album( #4
        title='The Last Goodbye',
        artist_id=4,
        user_id=1,
        image_url='https://yuhtube-bucket.s3.amazonaws.com/album-seeds/thelastgoodbye-album.jpg'
    ),
    Album( #5
        title='Love Is Alive',
        artist_id=5,
        user_id=1,
        image_url='https://yuhtube-bucket.s3.amazonaws.com/album-seeds/loveisalive-album.jpg'
    ),
    Album( #6
        title='Cartel II',
        artist_id=6,
        user_id=1,
        image_url='https://yuhtube-bucket.s3.amazonaws.com/album-seeds/cartelii-album.jpg'
    ),
    Album( #7
        title='GABRIEL',
        artist_id=7,
        user_id=1,
        image_url='https://yuhtube-bucket.s3.amazonaws.com/album-seeds/keshi-album.png'
    ),
    Album( #8
        title='The Cure To Loneliness',
        artist_id=8,
        user_id=1,
        image_url='https://yuhtube-bucket.s3.amazonaws.com/album-seeds/thecuretoloneliness-album.jpg'
    ),
    Album( #9
        title="The People's Champ",
        artist_id=9,
        user_id=1,
        image_url='https://yuhtube-bucket.s3.amazonaws.com/album-seeds/thepeopleschamp-album.jpg'
    ),
    Album( #10
        title='Lost',
        artist_id=10,
        user_id=1,
        image_url='https://yuhtube-bucket.s3.amazonaws.com/album-seeds/lost-album.jpg'
    ),
    Album( #11
        title='brent',
        artist_id=11,
        user_id=1,
        image_url='https://yuhtube-bucket.s3.amazonaws.com/album-seeds/brent-album.jpg'
    ),
    Album( #12
        title='For Lack of a Better Name',
        artist_id=12,
        user_id=1,
        image_url='https://yuhtube-bucket.s3.amazonaws.com/album-seeds/forlackofabettername-album.jpg'
    ),
]


def seed_albums():

    for album in albums:
        add_likes_to_albums(album)

        db.session.add(album)

    db.session.commit()


def undo_albums():
    db.session.execute('TRUNCATE albums RESTART IDENTITY CASCADE;')
    db.session.commit()
