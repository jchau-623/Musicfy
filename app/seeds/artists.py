from app.models import db, Artist

artists = [
    Artist( #1
        name='Seven Lions',
    ),
    Artist( #2
        name='Illenium',
    ),
    Artist( #3
        name='What So Not',
    ),
    Artist( #4
        name='Odesza',
    ),
    Artist(#5
        name='Louis The Child'
    ),
    Artist(#6
        name='Boombox Cartel'
    ),
    Artist(#7
        name='Keshi'
    ),
    Artist(#8
        name='Jai Wolf'
    ),
    Artist(#9
        name='Quinn XCII'
    ),
    Artist(#10
        name='Mitis'
    ),
    Artist(#11
        name='Chelsea Cutler'
    ),
    Artist(#12
        name='deadmau5'
    ),
]

def seed_artists():
    for artist in artists:
        db.session.add(artist)

    db.session.commit()

def undo_artists():
    db.session.execute('TRUNCATE artists RESTART IDENTITY CASCADE;')
    db.session.commit()
