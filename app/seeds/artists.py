from app.models import db, Artist

artists = [
    Artist(#1
        name='Seven Lions',
        image_url='https://yuhtube-bucket.s3.amazonaws.com/artists-seeds/seven-lions-propic.jpg'
    ),
    Artist(#2
        name='Illenium',
        image_url='https://yuhtube-bucket.s3.amazonaws.com/artists-seeds/illenium-propic.jpg'
    ),
    Artist(#3
        name='What So Not',
        image_url='https://yuhtube-bucket.s3.amazonaws.com/artists-seeds/whatsonot-propic.jpg'
    ),
    Artist(#4
        name='Odesza',
        image_url='https://yuhtube-bucket.s3.amazonaws.com/artists-seeds/odesza-propic.jpg'
    ),
    Artist(#5
        name='Louis The Child',
        image_url='https://yuhtube-bucket.s3.amazonaws.com/artists-seeds/louis-the-child-propic.png'
    ),
    Artist(#6
        name='Boombox Cartel',
        image_url='https://yuhtube-bucket.s3.amazonaws.com/artists-seeds/boombox-cartel-propic.jpg'
    ),
    Artist(#7
        name='Keshi',
        image_url='https://yuhtube-bucket.s3.amazonaws.com/artists-seeds/keshi-propic.png'
    ),
    Artist(#8
        name='Jai Wolf',
        image_url='https://yuhtube-bucket.s3.amazonaws.com/artists-seeds/jaiwolf-propic.jpg'
    ),
    Artist(#9
        name='Quinn XCII',
        image_url='https://yuhtube-bucket.s3.amazonaws.com/artists-seeds/quinnxcii-propic.jpg'
    ),
    Artist(#10
        name='Mitis',
        image_url='https://yuhtube-bucket.s3.amazonaws.com/artists-seeds/mitis-propic.jpg'
    ),
    Artist(#11
        name='Chelsea Cutler',
        image_url='https://yuhtube-bucket.s3.amazonaws.com/artists-seeds/chelsea-cutler-propic.jpg'
    ),
    Artist(#12
        name='deadmau5',
        image_url='https://yuhtube-bucket.s3.amazonaws.com/artists-seeds/deadmau5-propic.jpg'
    ),
]

def seed_artists():
    for artist in artists:
        db.session.add(artist)

    db.session.commit()

def undo_artists():
    db.session.execute('TRUNCATE artists RESTART IDENTITY CASCADE;')
    db.session.commit()
