from app.models import db, Song

songs = [
    Song( #1
        title='Prologue',
        user_id=1,
        artist_id=1,
        song_url='https://yuhtube-bucket.s3.amazonaws.com/songs-seeds/Seven_Lions_Prologue.mp3',
        image_url='https://yuhtube-bucket.s3.amazonaws.com/album-seeds/beyondtheveil-album.jpg',
        track_number=1,
        album_id=1
    ),
    Song( #2
        title='Call On Me (feat. Vancouver Sleep Clinic)',
        user_id=1,
        artist_id=1,
        song_url='https://yuhtube-bucket.s3.amazonaws.com/songs-seeds/Seven_Lions_Call_On_Me_feat_Vancouver_Sleep_Clinic.mp3',
        image_url='https://yuhtube-bucket.s3.amazonaws.com/album-seeds/beyondtheveil-album.jpg',
        track_number=2,
        album_id=1
    ),
    Song( #3
        title='Every Time (feat. So Below)',
        user_id=1,
        artist_id=1,
        song_url='https://yuhtube-bucket.s3.amazonaws.com/songs-seeds/Seven_Lions_Every_Time_feat_So_Below_.mp3',
        image_url='https://yuhtube-bucket.s3.amazonaws.com/album-seeds/beyondtheveil-album.jpg',
        track_number=3,
        album_id=1
    ),
    Song( #4
        title='Between (feat. Eli Teplin)',
        user_id=1,
        artist_id=1,
        song_url='https://yuhtube-bucket.s3.amazonaws.com/songs-seeds/Seven_Lions_Between_feat_Eli_Teplin_.mp3',
        image_url='https://yuhtube-bucket.s3.amazonaws.com/album-seeds/beyondtheveil-album.jpg',
        track_number=4,
        album_id=1
    ),
    Song( #5
        title='Someday',
        user_id=1,
        artist_id=1,
        song_url='https://yuhtube-bucket.s3.amazonaws.com/songs-seeds/Seven_Lions_Someday.mp3',
        image_url='https://yuhtube-bucket.s3.amazonaws.com/album-seeds/beyondtheveil-album.jpg',
        track_number=5,
        album_id=1
    ),
    Song( #6
        title='Miss You (feat. GG Magree)',
        user_id=1,
        artist_id=1,
        song_url='https://yuhtube-bucket.s3.amazonaws.com/songs-seeds/Seven_Lions_Miss_You_feat_GG_Magree_.mp3',
        image_url='https://yuhtube-bucket.s3.amazonaws.com/album-seeds/beyondtheveil-album.jpg',
        track_number=6,
        album_id=1
    ),
    Song( #7
        title='Beyond The Veil (feat. JT Roach)',
        user_id=1,
        artist_id=1,
        song_url='https://yuhtube-bucket.s3.amazonaws.com/songs-seeds/Seven_Lions_Beyond_The_Veil_feat_JT_Roach_.mp3',
        image_url='https://yuhtube-bucket.s3.amazonaws.com/album-seeds/beyondtheveil-album.jpg',
        track_number=7,
        album_id=1
    ),
    Song( #8
        title='Before You (feat. Dia Frampton)',
        user_id=1,
        artist_id=1,
        song_url='https://yuhtube-bucket.s3.amazonaws.com/songs-seeds/Seven_Lions_Before_You_feat_Dia_Frampton_.mp3',
        image_url='https://yuhtube-bucket.s3.amazonaws.com/album-seeds/beyondtheveil-album.jpg',
        track_number=8,
        album_id=1
    ),
    Song( #9
        title='Never Learn (feat. Mija)',
        user_id=1,
        artist_id=1,
        song_url='https://yuhtube-bucket.s3.amazonaws.com/songs-seeds/Seven_Lions_Never_Learn_feat_Mija_.mp3',
        image_url='https://yuhtube-bucket.s3.amazonaws.com/album-seeds/beyondtheveil-album.jpg',
        track_number=9,
        album_id=1
    ),
    Song( #10
        title='Stop Thinking (feat. Lights)',
        user_id=1,
        artist_id=1,
        song_url='https://yuhtube-bucket.s3.amazonaws.com/songs-seeds/Seven_Lions_Stop_Thinking_feat_Lights_.mp3',
        image_url='https://yuhtube-bucket.s3.amazonaws.com/album-seeds/beyondtheveil-album.jpg',
        track_number=10,
        album_id=1
    ),
    Song( #11
        title='Falling Fast (feat. Dia Frampton)',
        user_id=1,
        artist_id=1,
        song_url='https://yuhtube-bucket.s3.amazonaws.com/songs-seeds/Seven_Lions_Falling_Fast_feat_GG_Magree_.mp3',
        image_url='https://yuhtube-bucket.s3.amazonaws.com/album-seeds/beyondtheveil-album.jpg',
        track_number=11,
        album_id=1
    ),
    Song( #12
        title='Henosis',
        user_id=1,
        artist_id=1,
        song_url='https://yuhtube-bucket.s3.amazonaws.com/songs-seeds/Seven_Lions_Henosis.mp3',
        image_url='https://yuhtube-bucket.s3.amazonaws.com/album-seeds/beyondtheveil-album.jpg',
        track_number=12,
        album_id=1
    ),
    Song( #13
        title='Alive (feat. Opposite the Other)',
        user_id=1,
        artist_id=1,
        song_url='https://yuhtube-bucket.s3.amazonaws.com/songs-seeds/Seven_Lions_Alive_feat_Opposite_the_Other_.mp3',
        image_url='https://yuhtube-bucket.s3.amazonaws.com/album-seeds/beyondtheveil-album.jpg',
        track_number=13,
        album_id=1
    ),
    Song( #14
        title='Brightest Light (feat. Dotter)',
        user_id=1,
        artist_id=1,
        song_url='https://yuhtube-bucket.s3.amazonaws.com/songs-seeds/Seven_Lions_Brightest_Light_feat_Dotter_.mp3',
        image_url='https://yuhtube-bucket.s3.amazonaws.com/album-seeds/beyondtheveil-album.jpg',
        track_number=14,
        album_id=1
    ),
    Song( #15
        title='Reverie',
        user_id=1,
        artist_id=2,
        song_url='https://yuhtube-bucket.s3.amazonaws.com/songs-seeds/Illenium_Reverie.mp3',
        image_url='https://yuhtube-bucket.s3.amazonaws.com/album-seeds/ashes-album.jpg',
        track_number=1,
        album_id=2
    ),
    Song( #16
        title='Fortress',
        user_id=1,
        artist_id=2,
        song_url='https://yuhtube-bucket.s3.amazonaws.com/songs-seeds/Illenium_Fortress.mp3',
        image_url='https://yuhtube-bucket.s3.amazonaws.com/album-seeds/ashes-album.jpg',
        track_number=2,
        album_id=2
    ),
    Song( #17
        title='With You',
        user_id=1,
        artist_id=2,
        song_url='https://yuhtube-bucket.s3.amazonaws.com/songs-seeds/Illenium_With_You.mp3',
        image_url='https://yuhtube-bucket.s3.amazonaws.com/album-seeds/ashes-album.jpg',
        track_number=3,
        album_id=2
    ),
    Song( #18
        title='Sleepwalker',
        user_id=1,
        artist_id=2,
        song_url='https://yuhtube-bucket.s3.amazonaws.com/songs-seeds/Illenium_Sleepwalker.mp3',
        image_url='https://yuhtube-bucket.s3.amazonaws.com/album-seeds/ashes-album.jpg',
        track_number=4,
        album_id=2
    ),
    Song( #19
        title="It's All on U",
        user_id=1,
        artist_id=2,
        song_url='https://yuhtube-bucket.s3.amazonaws.com/songs-seeds/Illenium_It%E2%80%99s_All_on_U.mp3',
        image_url='https://yuhtube-bucket.s3.amazonaws.com/album-seeds/ashes-album.jpg',
        track_number=5,
        album_id=2
    ),
    Song( #20
        title='Spirals',
        user_id=1,
        artist_id=2,
        song_url='https://yuhtube-bucket.s3.amazonaws.com/songs-seeds/Illenium_Spirals.mp3',
        image_url='https://yuhtube-bucket.s3.amazonaws.com/album-seeds/ashes-album.jpg',
        track_number=6,
        album_id=2
    ),
    Song( #21
        title='Without You',
        user_id=1,
        artist_id=2,
        song_url='https://yuhtube-bucket.s3.amazonaws.com/songs-seeds/Illenium_Without_You.mp3',
        image_url='https://yuhtube-bucket.s3.amazonaws.com/album-seeds/ashes-album.jpg',
        track_number=7,
        album_id=2
    ),
    Song( #22
        title='Only One',
        user_id=1,
        artist_id=2,
        song_url='https://yuhtube-bucket.s3.amazonaws.com/songs-seeds/Illenium_Only_One.mp3',
        image_url='https://yuhtube-bucket.s3.amazonaws.com/album-seeds/ashes-album.jpg',
        track_number=8,
        album_id=2
    ),
    Song( #23
        title="I'll Be Your Reason",
        user_id=1,
        artist_id=2,
        song_url='https://yuhtube-bucket.s3.amazonaws.com/songs-seeds/Illenium_I_ll_Be_Your_Reason.mp3',
        image_url='https://yuhtube-bucket.s3.amazonaws.com/album-seeds/ashes-album.jpg',
        track_number=9,
        album_id=2
    ),
    Song( #24
        title='Afterlife',
        user_id=1,
        artist_id=2,
        song_url='https://yuhtube-bucket.s3.amazonaws.com/songs-seeds/Illenium_Afterlife.mp3',
        image_url='https://yuhtube-bucket.s3.amazonaws.com/album-seeds/ashes-album.jpg',
        track_number=10,
        album_id=2
    ),
    Song( #25
        title='Alive',
        user_id=1,
        artist_id=3,
        song_url='',
        image_url='https://yuhtube-bucket.s3.amazonaws.com/album-seeds/anomaly-album.jpg',
        track_number=1,
        album_id=3
    ),
    Song( #26
        title='Anomaly',
        user_id=1,
        artist_id=3,
        song_url='',
        image_url='https://yuhtube-bucket.s3.amazonaws.com/album-seeds/anomaly-album.jpg',
        track_number=2,
        album_id=3
    ),
    Song( #27
        title='Mr Regular',
        user_id=1,
        artist_id=3,
        song_url='',
        image_url='https://yuhtube-bucket.s3.amazonaws.com/album-seeds/anomaly-album.jpg',
        track_number=3,
        album_id=3
    ),
    Song( #25
        title='The Change',
        user_id=1,
        artist_id=3,
        song_url='',
        image_url='https://yuhtube-bucket.s3.amazonaws.com/album-seeds/anomaly-album.jpg',
        track_number=4,
        album_id=3
    ),
    Song( #25
        title='Halifax',
        user_id=1,
        artist_id=3,
        song_url='',
        image_url='https://yuhtube-bucket.s3.amazonaws.com/album-seeds/anomaly-album.jpg',
        track_number=5,
        album_id=3
    ),
    Song( #25
        title='On Air',
        user_id=1,
        artist_id=3,
        song_url='',
        image_url='https://yuhtube-bucket.s3.amazonaws.com/album-seeds/anomaly-album.jpg',
        track_number=6,
        album_id=3
    ),
    Song( #25
        title="Messin' Me up",
        user_id=1,
        artist_id=3,
        song_url='',
        image_url='https://yuhtube-bucket.s3.amazonaws.com/album-seeds/anomaly-album.jpg',
        track_number=7,
        album_id=3
    ),
    Song( #25
        title='Bad Piano',
        user_id=1,
        artist_id=3,
        song_url='',
        image_url='',
        track_number=8,
        album_id=3
    ),
    Song( #25
        title='Mercy (2022 Edit)',
        user_id=1,
        artist_id=3,
        song_url='',
        image_url='',
        track_number=9,
        album_id=3
    ),
    Song( #25
        title='Black Shallow',
        user_id=1,
        artist_id=3,
        song_url='',
        image_url='',
        track_number=10,
        album_id=3
    ),
    Song( #25
        title='As One',
        user_id=1,
        artist_id=3,
        song_url='',
        image_url='',
        track_number=11,
        album_id=3
    ),
]

def seed_songs():
    for song in songs:
        db.session.add(song)



    db.session.commit()


def undo_songs():
    db.session.execute('TRUNCATE songs RESTART IDENTITY CASCADE;')
    db.session.commit()
