from app.models import db, Song
from app.seeds.song_likes import add_likes_to_songs

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
        song_url='https://yuhtube-bucket.s3.amazonaws.com/songs-seeds/What+So+Not+-++Alive++(Official+Audio).mp3',
        image_url='https://yuhtube-bucket.s3.amazonaws.com/album-seeds/anomaly-album.jpg',
        track_number=1,
        album_id=3
    ),
    Song( #26
        title='Anomaly',
        user_id=1,
        artist_id=3,
        song_url='https://yuhtube-bucket.s3.amazonaws.com/songs-seeds/What+So+Not+-++Anomaly+(feat.+AY+AY)++(Official+Audio).mp3',
        image_url='https://yuhtube-bucket.s3.amazonaws.com/album-seeds/anomaly-album.jpg',
        track_number=2,
        album_id=3
    ),
    Song( #27
        title='Mr Regular',
        user_id=1,
        artist_id=3,
        song_url='https://yuhtube-bucket.s3.amazonaws.com/songs-seeds/What+So+Not+-++Mr+Regular+(feat.+Oliver+Tree%2C+Killer+Mike)++(Official+Audio).mp3',
        image_url='https://yuhtube-bucket.s3.amazonaws.com/album-seeds/anomaly-album.jpg',
        track_number=3,
        album_id=3
    ),
    Song( #28
        title='The Change',
        user_id=1,
        artist_id=3,
        song_url='https://yuhtube-bucket.s3.amazonaws.com/songs-seeds/What+So+Not+-+The+Change+(Feat.+DMA+S).mp3',
        image_url='https://yuhtube-bucket.s3.amazonaws.com/album-seeds/anomaly-album.jpg',
        track_number=4,
        album_id=3
    ),
    Song( #29
        title='Halifax',
        user_id=1,
        artist_id=3,
        song_url="https://yuhtube-bucket.s3.amazonaws.com/songs-seeds/What+So+Not+-+'Halifax+(feat.+ZOID+LAND%2C+Phi11a%2C+Tek+Genesis)'+(Official+Audio).mp3",
        image_url='https://yuhtube-bucket.s3.amazonaws.com/album-seeds/anomaly-album.jpg',
        track_number=5,
        album_id=3
    ),
    Song( #30
        title='On Air',
        user_id=1,
        artist_id=3,
        song_url="https://yuhtube-bucket.s3.amazonaws.com/songs-seeds/What+So+Not+-+'On+Air+(feat.+Louis+The+Child%2C+Captain+Cuts%2C+JRM)'++(Official+Audio).mp3",
        image_url='https://yuhtube-bucket.s3.amazonaws.com/album-seeds/anomaly-album.jpg',
        track_number=6,
        album_id=3
    ),
    Song( #31
        title="Messin' Me up",
        user_id=1,
        artist_id=3,
        song_url="https://yuhtube-bucket.s3.amazonaws.com/songs-seeds/What+So+Not+-+Messin'+Me+Up+(feat.+EVAN+GIIA)+%5BOfficial+Music+Video%5D.mp3",
        image_url='https://yuhtube-bucket.s3.amazonaws.com/album-seeds/anomaly-album.jpg',
        track_number=7,
        album_id=3
    ),
    Song( #32
        title='Bad Piano',
        user_id=1,
        artist_id=3,
        song_url="https://yuhtube-bucket.s3.amazonaws.com/songs-seeds/What+So+Not+-+'Bad+Piano+(feat.+Body+Ocean%2C+Lucy+Lucy)'+(Official+Audio).mp3",
        image_url='https://yuhtube-bucket.s3.amazonaws.com/album-seeds/anomaly-album.jpg',
        track_number=8,
        album_id=3
    ),
    Song( #33
        title='Mercy (2022 Edit)',
        user_id=1,
        artist_id=3,
        song_url="https://yuhtube-bucket.s3.amazonaws.com/songs-seeds/What+So+Not+-+'Mercy+(2022+Edit+feat.+M%C3%98)'+(Official+Audio).mp3",
        image_url='https://yuhtube-bucket.s3.amazonaws.com/album-seeds/anomaly-album.jpg',
        track_number=9,
        album_id=3
    ),
    Song( #34
        title='Black Shallow',
        user_id=1,
        artist_id=3,
        song_url="https://yuhtube-bucket.s3.amazonaws.com/songs-seeds/What+So+Not+-+'Black+Shallow+(feat.+Enschway)'+(Official+Audio).mp3",
        image_url='https://yuhtube-bucket.s3.amazonaws.com/album-seeds/anomaly-album.jpg',
        track_number=10,
        album_id=3
    ),
    Song( #35
        title='As One',
        user_id=1,
        artist_id=3,
        song_url="https://yuhtube-bucket.s3.amazonaws.com/songs-seeds/What+So+Not+-+'As+One+(feat.+Herizen)'++(Official+Audio).mp3",
        image_url="https://yuhtube-bucket.s3.amazonaws.com/album-seeds/anomaly-album.jpg",
        track_number=11,
        album_id=3
    ),
    Song( #36
        title='This Version Of You (feat. Julianna Barwick)',
        user_id=1,
        artist_id=4,
        song_url="https://yuhtube-bucket.s3.amazonaws.com/songs-seeds/ODESZA+-+This+Version+Of+You+(feat.+Julianna+Barwick)+-+Official+Audio.mp3",
        image_url="https://yuhtube-bucket.s3.amazonaws.com/album-seeds/thelastgoodbye-album.jpg",
        track_number=1,
        album_id=4
    ),
    Song( #37
        title='Wide Awake (feat. Charlie Houston)',
        user_id=1,
        artist_id=4,
        song_url="https://yuhtube-bucket.s3.amazonaws.com/songs-seeds/ODESZA+-+Wide+Awake+(feat.+Charlie+Houston)+-+Official+Audio.mp3",
        image_url="https://yuhtube-bucket.s3.amazonaws.com/album-seeds/thelastgoodbye-album.jpg",
        track_number=2,
        album_id=4
    ),
    Song( #38
        title='Love Letter (feat. The Knocks)',
        user_id=1,
        artist_id=4,
        song_url="https://yuhtube-bucket.s3.amazonaws.com/songs-seeds/ODESZA+-+Love+Letter+(feat.+The+Knocks)+-+Official+Audio.mp3",
        image_url="https://yuhtube-bucket.s3.amazonaws.com/album-seeds/thelastgoodbye-album.jpg",
        track_number=3,
        album_id=4
    ),
    Song( #39
        title='Behind The Sun',
        user_id=1,
        artist_id=4,
        song_url="https://yuhtube-bucket.s3.amazonaws.com/songs-seeds/ODESZA+-+Behind+The+Sun+-+Official+Video.mp3",
        image_url="https://yuhtube-bucket.s3.amazonaws.com/album-seeds/thelastgoodbye-album.jpg",
        track_number=4,
        album_id=4
    ),
    Song( #40
        title='Forgive Me (feat. Izy Bizu)',
        user_id=1,
        artist_id=4,
        song_url="https://yuhtube-bucket.s3.amazonaws.com/songs-seeds/ODESZA+-+Forgive+Me+(feat.+Izzy+Bizu)+-+Official+Audio.mp3",
        image_url="https://yuhtube-bucket.s3.amazonaws.com/album-seeds/thelastgoodbye-album.jpg",
        track_number=5,
        album_id=4
    ),
    Song( #41
        title='North Garden',
        user_id=1,
        artist_id=4,
        song_url="https://yuhtube-bucket.s3.amazonaws.com/songs-seeds/ODESZA+-+North+Garden+-+Official+Audio.mp3",
        image_url="https://yuhtube-bucket.s3.amazonaws.com/album-seeds/thelastgoodbye-album.jpg",
        track_number=6,
        album_id=4
    ),
    Song( #42
        title='Better Now (feat. MARO)',
        user_id=1,
        artist_id=4,
        song_url="https://yuhtube-bucket.s3.amazonaws.com/songs-seeds/ODESZA+-+Better+Now+(feat.+MARO)+-+Official+Video.mp3",
        image_url="https://yuhtube-bucket.s3.amazonaws.com/album-seeds/thelastgoodbye-album.jpg",
        track_number=7,
        album_id=4
    ),
    Song( #43
        title='The Last Goodbye (feat. Bettye LaVette)',
        user_id=1,
        artist_id=4,
        song_url="",
        image_url="https://yuhtube-bucket.s3.amazonaws.com/album-seeds/thelastgoodbye-album.jpg",
        track_number=8,
        album_id=4
    ),
    Song( #44
        title='All My Life',
        user_id=1,
        artist_id=4,
        song_url="https://yuhtube-bucket.s3.amazonaws.com/songs-seeds/ODESZA+-+The+Last+Goodbye+(feat.+Bettye+LaVette)+-+Official+Visualizer.mp3",
        image_url="https://yuhtube-bucket.s3.amazonaws.com/album-seeds/thelastgoodbye-album.jpg",
        track_number=9,
        album_id=4
    ),
    Song( #45
        title='Equal (feat. Låpsley)',
        user_id=1,
        artist_id=4,
        song_url="https://yuhtube-bucket.s3.amazonaws.com/songs-seeds/ODESZA+-+Equal+(feat.+L%C3%A5psley)+-+Official+Audio.mp3",
        image_url="https://yuhtube-bucket.s3.amazonaws.com/album-seeds/thelastgoodbye-album.jpg",
        track_number=10,
        album_id=4
    ),
    Song( #46
        title='Healing Grid',
        user_id=1,
        artist_id=4,
        song_url="https://yuhtube-bucket.s3.amazonaws.com/songs-seeds/ODESZA+-+Healing+Grid+-+Official+Audio.mp3",
        image_url="https://yuhtube-bucket.s3.amazonaws.com/album-seeds/thelastgoodbye-album.jpg",
        track_number=11,
        album_id=4
    ),
    Song( #47
        title="I Can't Sleep",
        user_id=1,
        artist_id=4,
        song_url="https://yuhtube-bucket.s3.amazonaws.com/songs-seeds/ODESZA+-+I+Cant+Sleep+-+Official+Audio.mp3",
        image_url="https://yuhtube-bucket.s3.amazonaws.com/album-seeds/thelastgoodbye-album.jpg",
        track_number=12,
        album_id=4
    ),
    Song( #48
        title='Light Of Day (feat. Ólafur Arnalds)',
        user_id=1,
        artist_id=4,
        song_url="https://yuhtube-bucket.s3.amazonaws.com/songs-seeds/ODESZA+-+Light+Of+Day+(feat.+%C3%93lafur+Arnalds)+-+Official+Video.mp3",
        image_url="https://yuhtube-bucket.s3.amazonaws.com/album-seeds/thelastgoodbye-album.jpg",
        track_number=13,
        album_id=4
    ),
    Song( #49
        title='Go',
        user_id=1,
        artist_id=5,
        song_url="https://yuhtube-bucket.s3.amazonaws.com/songs-seeds/Louis+The+Child+-+Go.mp3",
        image_url="https://yuhtube-bucket.s3.amazonaws.com/album-seeds/loveisalive-album.jpg",
        track_number=1,
        album_id=5
    ),
    Song( #50
        title='Fire',
        user_id=1,
        artist_id=5,
        song_url="https://yuhtube-bucket.s3.amazonaws.com/songs-seeds/Louis+The+Child+-+Fire+(ft.+Evalyn).mp3",
        image_url="https://yuhtube-bucket.s3.amazonaws.com/album-seeds/loveisalive-album.jpg",
        track_number=2,
        album_id=5
    ),
    Song( #51
        title='Slow Down Love',
        user_id=1,
        artist_id=5,
        song_url="https://yuhtube-bucket.s3.amazonaws.com/songs-seeds/Louis+The+Child+-+Slow+Down+Love+feat.+Chelsea+Cutler+(Cover+Art).mp3",
        image_url="https://yuhtube-bucket.s3.amazonaws.com/album-seeds/loveisalive-album.jpg",
        track_number=3,
        album_id=5
    ),
    Song( #52
        title='Phone Died',
        user_id=1,
        artist_id=5,
        song_url="https://yuhtube-bucket.s3.amazonaws.com/songs-seeds/Louis+The+Child+-+Phone+Died+(feat.+Blaise+Railey).mp3",
        image_url="https://yuhtube-bucket.s3.amazonaws.com/album-seeds/loveisalive-album.jpg",
        track_number=4,
        album_id=5
    ),
    Song( #53
        title='World On Fire',
        user_id=1,
        artist_id=5,
        song_url="https://yuhtube-bucket.s3.amazonaws.com/songs-seeds/Louis+The+Child+-+World+On+Fire+feat.+Ashe+(Cover+Art).mp3",
        image_url="https://yuhtube-bucket.s3.amazonaws.com/album-seeds/loveisalive-album.jpg",
        track_number=5,
        album_id=5
    ),
    Song( #54
        title='Love Is Alive',
        user_id=1,
        artist_id=5,
        song_url="https://yuhtube-bucket.s3.amazonaws.com/songs-seeds/Louis+The+Child+-+Love+Is+Alive+ft.+Elohim.mp3",
        image_url="https://yuhtube-bucket.s3.amazonaws.com/album-seeds/loveisalive-album.jpg",
        track_number=6,
        album_id=5
    ),
    Song( #55
        title='MONTA',
        user_id=1,
        artist_id=6,
        song_url="https://yuhtube-bucket.s3.amazonaws.com/songs-seeds/Boombox+Cartel+-+MONTA+(Official+Audio).mp3",
        image_url="https://yuhtube-bucket.s3.amazonaws.com/album-seeds/cartelii-album.jpg",
        track_number=1,
        album_id=6
    ),
    Song( #56
        title='Máquina',
        user_id=1,
        artist_id=6,
        song_url="https://yuhtube-bucket.s3.amazonaws.com/songs-seeds/Boombox+Cartel+-+M%C3%A1quina+(Official+Audio).mp3",
        image_url="https://yuhtube-bucket.s3.amazonaws.com/album-seeds/cartelii-album.jpg",
        track_number=2,
        album_id=6
    ),
    Song( #57
        title='Shadow (feat. Calivania)',
        user_id=1,
        artist_id=6,
        song_url="https://yuhtube-bucket.s3.amazonaws.com/songs-seeds/Boombox+Cartel+x+Moody+Good+-+Shadow+(feat.+Calivania)+%5BOfficial+Music+Video%5D.mp3",
        image_url="https://yuhtube-bucket.s3.amazonaws.com/album-seeds/cartelii-album.jpg",
        track_number=3,
        album_id=6
    ),
    Song( #58
        title='Rock Dem',
        user_id=1,
        artist_id=6,
        song_url="https://yuhtube-bucket.s3.amazonaws.com/songs-seeds/Boombox+Cartel+-+Rock+Dem+(Official+Audio).mp3",
        image_url="https://yuhtube-bucket.s3.amazonaws.com/album-seeds/cartelii-album.jpg",
        track_number=4,
        album_id=6
    ),
    Song( #59
        title='Fatal Attraction (feat. Reese LAFLARE)',
        artist_id=6,
        song_url="https://yuhtube-bucket.s3.amazonaws.com/songs-seeds/Boombox+Cartel+-+Fatal+Attraction+(feat.+Reese+LAFLARE)+%5BOfficial+Audio%5D.mp3",
        image_url="https://yuhtube-bucket.s3.amazonaws.com/album-seeds/cartelii-album.jpg",
        track_number=5,
        album_id=6
    ),
    Song( #60
        title='Reaper (feat. JID)',
        user_id=1,
        artist_id=6,
        song_url="https://yuhtube-bucket.s3.amazonaws.com/songs-seeds/Boombox+Cartel+-+Reaper+(feat.+JID)+%5BOfficial+Audio%5D.mp3",
        image_url="https://yuhtube-bucket.s3.amazonaws.com/album-seeds/cartelii-album.jpg",
        track_number=6,
        album_id=6
    ),
    Song( #61
        title='Veneno',
        user_id=1,
        artist_id=6,
        song_url="https://yuhtube-bucket.s3.amazonaws.com/songs-seeds/Boombox+Cartel+-+Veneno+(Official+Audio).mp3",
        image_url="https://yuhtube-bucket.s3.amazonaws.com/album-seeds/cartelii-album.jpg",
        track_number=7,
        album_id=6
    ),
    Song( #62
        title='GET IT',
        user_id=1,
        artist_id=7,
        song_url="https://yuhtube-bucket.s3.amazonaws.com/songs-seeds/keshi+-+GET+IT.mp3",
        image_url="https://yuhtube-bucket.s3.amazonaws.com/album-seeds/keshi-album.png",
        track_number=1,
        album_id=7
    ),
    Song( #63
        title='SOMEBODY',
        user_id=1,
        artist_id=7,
        song_url="https://yuhtube-bucket.s3.amazonaws.com/songs-seeds/keshi+-+SOMEBODY.mp3",
        image_url="https://yuhtube-bucket.s3.amazonaws.com/album-seeds/keshi-album.png",
        track_number=2,
        album_id=7
    ),
    Song( #64
        title='WESTSIDE',
        user_id=1,
        artist_id=7,
        song_url="https://yuhtube-bucket.s3.amazonaws.com/songs-seeds/keshi+-+WESTSIDE.mp3",
        image_url="https://yuhtube-bucket.s3.amazonaws.com/album-seeds/keshi-album.png",
        track_number=3,
        album_id=7
    ),
    Song( #65
        title='TOUCH',
        user_id=1,
        artist_id=7,
        song_url="https://yuhtube-bucket.s3.amazonaws.com/songs-seeds/keshi+-+TOUCH+(Official+Audio).mp3",
        image_url="https://yuhtube-bucket.s3.amazonaws.com/album-seeds/keshi-album.png",
        track_number=4,
        album_id=7
    ),
    Song( #66
        title='MILLI',
        user_id=1,
        artist_id=7,
        song_url="https://yuhtube-bucket.s3.amazonaws.com/songs-seeds/keshi+-+MILLI+(Visualizer).mp3",
        image_url="https://yuhtube-bucket.s3.amazonaws.com/album-seeds/keshi-album.png",
        track_number=5,
        album_id=7
    ),
    Song( #67
        title='PÈRE',
        user_id=1,
        artist_id=7,
        song_url="https://yuhtube-bucket.s3.amazonaws.com/songs-seeds/keshi+-+P%C3%88RE+(Visualizer).mp3",
        image_url="https://yuhtube-bucket.s3.amazonaws.com/album-seeds/keshi-album.png",
        track_number=6,
        album_id=7
    ),
    Song( #68
        title='HELL/HEAVEN',
        user_id=1,
        artist_id=7,
        song_url="https://yuhtube-bucket.s3.amazonaws.com/songs-seeds/keshi+-+HELLHEAVEN+(Visualizer).mp3",
        image_url="https://yuhtube-bucket.s3.amazonaws.com/album-seeds/keshi-album.png",
        track_number=7,
        album_id=7
    ),
    Song( #69
        title='ANGOSTURA',
        user_id=1,
        artist_id=7,
        song_url="https://yuhtube-bucket.s3.amazonaws.com/songs-seeds/ANGOSTURA.mp3",
        image_url="https://yuhtube-bucket.s3.amazonaws.com/album-seeds/keshi-album.png",
        track_number=8,
        album_id=7
    ),
    Song( #70
        title='UNDERSTAND',
        user_id=1,
        artist_id=7,
        song_url="https://yuhtube-bucket.s3.amazonaws.com/songs-seeds/keshi+-+UNDERSTAND+(Visualizer).mp3",
        image_url="https://yuhtube-bucket.s3.amazonaws.com/album-seeds/keshi-album.png",
        track_number=9,
        album_id=7
    ),
    Song( #71
        title='LIMBO',
        user_id=1,
        artist_id=7,
        song_url="https://yuhtube-bucket.s3.amazonaws.com/songs-seeds/keshi+-+LIMBO+(Visualizer).mp3",
        image_url="https://yuhtube-bucket.s3.amazonaws.com/album-seeds/keshi-album.png",
        track_number=10,
        album_id=7
    ),
    Song( #72
        title='ANGEL',
        user_id=1,
        artist_id=7,
        song_url="https://yuhtube-bucket.s3.amazonaws.com/songs-seeds/keshi+-+ANGEL+(Visualizer).mp3",
        image_url="https://yuhtube-bucket.s3.amazonaws.com/album-seeds/keshi-album.png",
        track_number=11,
        album_id=7
    ),
    Song( #73
        title='GABRIEL',
        user_id=1,
        artist_id=7,
        song_url="https://yuhtube-bucket.s3.amazonaws.com/songs-seeds/keshi+-+GABRIEL+(Visualizer).mp3",
        image_url="https://yuhtube-bucket.s3.amazonaws.com/album-seeds/keshi-album.png",
        track_number=12,
        album_id=7
    ),
    Song( #74
        title='Intro',
        user_id=1,
        artist_id=8,
        song_url="https://yuhtube-bucket.s3.amazonaws.com/songs-seeds/Jai+Wolf+-+Intro+(Official+Audio).mp3",
        image_url="https://yuhtube-bucket.s3.amazonaws.com/album-seeds/thecuretoloneliness-album.jpg",
        track_number=1,
        album_id=8
    ),
    Song( #75
        title='Lose My Mind (feat. Mr Gabriel)',
        user_id=1,
        artist_id=8,
        song_url="https://yuhtube-bucket.s3.amazonaws.com/songs-seeds/Jai+Wolf+-+Lose+My+Mind+(feat.+Mr.+Gabriel).mp3",
        image_url="https://yuhtube-bucket.s3.amazonaws.com/album-seeds/thecuretoloneliness-album.jpg",
        track_number=2,
        album_id=8
    ),
    Song( #76
        title='Telepathy',
        user_id=1,
        artist_id=8,
        song_url="https://yuhtube-bucket.s3.amazonaws.com/songs-seeds/Jai+Wolf+-+Telepathy+(Official+Visualizer).mp3",
        image_url="https://yuhtube-bucket.s3.amazonaws.com/album-seeds/thecuretoloneliness-album.jpg",
        track_number=3,
        album_id=8
    ),
    Song( #77
        title='Still Sleeping',
        user_id=1,
        artist_id=8,
        song_url="https://yuhtube-bucket.s3.amazonaws.com/songs-seeds/Jai+Wolf+-+Still+Sleeping+(Official+Audio).mp3",
        image_url="https://yuhtube-bucket.s3.amazonaws.com/album-seeds/thecuretoloneliness-album.jpg",
        track_number=4,
        album_id=8
    ),
    Song( #78
        title='This Song Reminds Me Of You',
        user_id=1,
        artist_id=8,
        song_url="https://yuhtube-bucket.s3.amazonaws.com/songs-seeds/Jai+Wolf+-+This+Song+Reminds+Me+Of+You+(Official+Audio).mp3",
        image_url="https://yuhtube-bucket.s3.amazonaws.com/album-seeds/thecuretoloneliness-album.jpg",
        track_number=5,
        album_id=8
    ),
    Song( #79
        title='Manic Pixie Dream',
        user_id=1,
        artist_id=8,
        song_url="https://yuhtube-bucket.s3.amazonaws.com/songs-seeds/Jai+Wolf+-+Manic+Pixie+Dream+(Official+Audio).mp3",
        image_url="https://yuhtube-bucket.s3.amazonaws.com/album-seeds/thecuretoloneliness-album.jpg",
        track_number=6,
        album_id=8
    ),
    Song( #80
        title='It All Started With A Feeling',
        user_id=1,
        artist_id=8,
        song_url="https://yuhtube-bucket.s3.amazonaws.com/songs-seeds/Jai+Wolf+-+It+All+Started+With+A+Feeling+(Official+Audio).mp3",
        image_url="https://yuhtube-bucket.s3.amazonaws.com/album-seeds/thecuretoloneliness-album.jpg",
        track_number=7,
        album_id=8
    ),
    Song( #81
        title='Better Apart (feat. Dresage)',
        user_id=1,
        artist_id=8,
        song_url="https://yuhtube-bucket.s3.amazonaws.com/songs-seeds/Jai+Wolf+-+Better+Apart+ft.+Dresage+(Official+Audio).mp3",
        image_url="https://yuhtube-bucket.s3.amazonaws.com/album-seeds/thecuretoloneliness-album.jpg",
        track_number=8,
        album_id=8
    ),
    Song( #82
        title='Drowning (feat. Robokid)',
        user_id=1,
        artist_id=8,
        song_url="https://yuhtube-bucket.s3.amazonaws.com/songs-seeds/Jai+Wolf+-+Drowning+ft.+Robokid+(Official+Audio).mp3",
        image_url="https://yuhtube-bucket.s3.amazonaws.com/album-seeds/thecuretoloneliness-album.jpg",
        track_number=9,
        album_id=8
    ),
    Song( #83
        title='Half Hearted Interlude',
        user_id=1,
        artist_id=8,
        song_url="https://yuhtube-bucket.s3.amazonaws.com/songs-seeds/Jai+Wolf+-+Half+Hearted+Interlude+(Official+Audio).mp3",
        image_url="https://yuhtube-bucket.s3.amazonaws.com/album-seeds/thecuretoloneliness-album.jpg",
        track_number=10,
        album_id=8
    ),
    Song( #84
        title='Your Way (feat. Day Wave)',
        user_id=1,
        artist_id=8,
        song_url="https://yuhtube-bucket.s3.amazonaws.com/songs-seeds/Jai+Wolf+-+Your+Way+ft.+Day+Wave+(Official+Lyric+Video).mp3",
        image_url="https://yuhtube-bucket.s3.amazonaws.com/album-seeds/thecuretoloneliness-album.jpg",
        track_number=11,
        album_id=8
    ),
    Song( #85
        title='Around The World (feat. Now, Now)',
        user_id=1,
        artist_id=8,
        song_url="https://yuhtube-bucket.s3.amazonaws.com/songs-seeds/Jai+Wolf+-+Around+the+World+ft.+Now%2C+Now+(Official+Audio).mp3",
        image_url="https://yuhtube-bucket.s3.amazonaws.com/album-seeds/thecuretoloneliness-album.jpg",
        track_number=12,
        album_id=8
    ),
    Song( #86
        title='Bartender',
        user_id=1,
        artist_id=9,
        song_url="https://yuhtube-bucket.s3.amazonaws.com/songs-seeds/Quinn+XCII+-+Bartender.mp3",
        image_url="https://yuhtube-bucket.s3.amazonaws.com/album-seeds/thepeopleschamp-album.jpg",
        track_number=1,
        album_id=9
    ),
    Song( #87
        title='Common (feat. Big Sean)',
        user_id=1,
        artist_id=9,
        song_url="https://yuhtube-bucket.s3.amazonaws.com/songs-seeds/Quinn+XCII+-+Common.mp3",
        image_url="https://yuhtube-bucket.s3.amazonaws.com/album-seeds/thepeopleschamp-album.jpg",
        track_number=2,
        album_id=9
    ),
    Song( #88
        title='Black Porsche',
        user_id=1,
        artist_id=9,
        song_url="https://yuhtube-bucket.s3.amazonaws.com/songs-seeds/Quinn+XCII+-+Black+Porsche.mp3",
        image_url="https://yuhtube-bucket.s3.amazonaws.com/album-seeds/thepeopleschamp-album.jpg",
        track_number=3,
        album_id=9
    ),
    Song( #89
        title="FOMO (Don't Do Cool Shit)",
        user_id=1,
        artist_id=9,
        song_url="https://yuhtube-bucket.s3.amazonaws.com/songs-seeds/Quinn+XCII+-+FOMO.mp3",
        image_url="https://yuhtube-bucket.s3.amazonaws.com/album-seeds/thepeopleschamp-album.jpg",
        track_number=4,
        album_id=9
    ),
    Song( #90
        title='Let Me Down (with Chelsea Cutler)',
        user_id=1,
        artist_id=9,
        song_url="https://yuhtube-bucket.s3.amazonaws.com/songs-seeds/Quinn+XCII+-+Let+Me+Down.mp3",
        image_url="https://yuhtube-bucket.s3.amazonaws.com/album-seeds/thepeopleschamp-album.jpg",
        track_number=5,
        album_id=9
    ),
    Song( #91
        title='Good Either Way (With Adrian Cota)',
        user_id=1,
        artist_id=9,
        song_url="https://yuhtube-bucket.s3.amazonaws.com/songs-seeds/Quinn+XCII+-+Good+Either+Way.mp3",
        image_url="https://yuhtube-bucket.s3.amazonaws.com/album-seeds/thepeopleschamp-album.jpg",
        track_number=6,
        album_id=9
    ),
    Song( #92
        title='Too Late (With AJR)',
        user_id=1,
        artist_id=9,
        song_url="https://yuhtube-bucket.s3.amazonaws.com/songs-seeds/Quinn+XCII+-+Too+Late.mp3",
        image_url="https://yuhtube-bucket.s3.amazonaws.com/album-seeds/thepeopleschamp-album.jpg",
        track_number=7,
        album_id=9
    ),
    Song( #93
        title='The Lows',
        user_id=1,
        artist_id=9,
        song_url="https://yuhtube-bucket.s3.amazonaws.com/songs-seeds/Quinn+XCII+-+The+Lows.mp3",
        image_url="https://yuhtube-bucket.s3.amazonaws.com/album-seeds/thepeopleschamp-album.jpg",
        track_number=8,
        album_id=9
    ),
    Song( #94
        title='Being Me',
        user_id=1,
        artist_id=9,
        song_url="https://yuhtube-bucket.s3.amazonaws.com/songs-seeds/Quinn+XCII+-+Being+Me.mp3",
        image_url="https://yuhtube-bucket.s3.amazonaws.com/album-seeds/thepeopleschamp-album.jpg",
        track_number=9,
        album_id=9
    ),
    Song( #95
        title='Why Do You Talk To Me?',
        user_id=1,
        artist_id=9,
        song_url="https://yuhtube-bucket.s3.amazonaws.com/songs-seeds/Quinn+XCII+-+Why+Do+You+Talk+To+Me.mp3",
        image_url="https://yuhtube-bucket.s3.amazonaws.com/album-seeds/thepeopleschamp-album.jpg",
        track_number=10,
        album_id=9
    ),
    Song( #96
        title='Backpack',
        user_id=1,
        artist_id=9,
        song_url="https://yuhtube-bucket.s3.amazonaws.com/songs-seeds/Quinn+XCII+-+Backpack.mp3",
        image_url="https://yuhtube-bucket.s3.amazonaws.com/album-seeds/thepeopleschamp-album.jpg",
        track_number=11,
        album_id=9
    ),
    Song( #97
        title='All That You Need',
        user_id=1,
        artist_id=9,
        song_url="https://yuhtube-bucket.s3.amazonaws.com/songs-seeds/Quinn+XCII+-+All+That+You+Need.mp3",
        image_url="https://yuhtube-bucket.s3.amazonaws.com/album-seeds/thepeopleschamp-album.jpg",
        track_number=12,
        album_id=9
    ),
    Song( #98
        title='Searching (Intro)',
        user_id=1,
        artist_id=10,
        song_url="https://yuhtube-bucket.s3.amazonaws.com/songs-seeds/MitiS+-+Searching+(Intro)++Ophelia+Records.mp3",
        image_url="https://yuhtube-bucket.s3.amazonaws.com/album-seeds/lost-album.jpg",
        track_number=1,
        album_id=10
    ),
    Song( #99
        title='Try (feat. RØRY)',
        user_id=1,
        artist_id=10,
        song_url="https://yuhtube-bucket.s3.amazonaws.com/songs-seeds/MitiS+-+Try+feat.+R%C3%98RY+%5BOfficial+Lyric+Video%5D.mp3",
        image_url="https://yuhtube-bucket.s3.amazonaws.com/album-seeds/lost-album.jpg",
        track_number=2,
        album_id=10
    ),
    Song( #100
        title='Homesick (feat. SOUNDR)',
        user_id=1,
        artist_id=10,
        song_url="https://yuhtube-bucket.s3.amazonaws.com/songs-seeds/MitiS+-+Homesick+feat.+SOUNDR+%5BOfficial+Lyric+Video%5D.mp3",
        image_url="https://yuhtube-bucket.s3.amazonaws.com/album-seeds/lost-album.jpg",
        track_number=3,
        album_id=10
    ),
    Song( #101
        title='Hurt (feat. Zack Gray)',
        user_id=1,
        artist_id=10,
        song_url="https://yuhtube-bucket.s3.amazonaws.com/songs-seeds/MitiS+-+Hurt+feat.+Zack+Gray++Ophelia+Records.mp3",
        image_url="https://yuhtube-bucket.s3.amazonaws.com/album-seeds/lost-album.jpg",
        track_number=4,
        album_id=10
    ),
    Song( #102
        title='Without Me (feat. Danni Carra)',
        user_id=1,
        artist_id=10,
        song_url="https://yuhtube-bucket.s3.amazonaws.com/songs-seeds/MitiS+-+Without+Me+(feat.+Danni+Carra)++Ophelia+Records.mp3",
        image_url="https://yuhtube-bucket.s3.amazonaws.com/album-seeds/lost-album.jpg",
        track_number=5,
        album_id=10
    ),
    Song( #103
        title='Bloom',
        user_id=1,
        artist_id=10,
        song_url="https://yuhtube-bucket.s3.amazonaws.com/songs-seeds/MitiS+-+Bloom++Ophelia+Records.mp3",
        image_url="https://yuhtube-bucket.s3.amazonaws.com/album-seeds/lost-album.jpg",
        track_number=6,
        album_id=10
    ),
    Song( #104
        title='Follow You',
        user_id=1,
        artist_id=10,
        song_url="https://yuhtube-bucket.s3.amazonaws.com/songs-seeds/MitiS+x+Rico+%26+Miella+-+Follow+You++Ophelia+Records.mp3",
        image_url="https://yuhtube-bucket.s3.amazonaws.com/album-seeds/lost-album.jpg",
        track_number=7,
        album_id=10
    ),
    Song( #105
        title="When I Say You're Mine (feat. Luma & Notelle)",
        user_id=1,
        artist_id=10,
        song_url="https://yuhtube-bucket.s3.amazonaws.com/songs-seeds/MitiS+-+When+I+Say+You're+Mine+(feat.+Luma+%26+Notelle)++Ophelia+Records.mp3",
        image_url="https://yuhtube-bucket.s3.amazonaws.com/album-seeds/lost-album.jpg",
        track_number=8,
        album_id=10
    ),
    Song( #106
        title='Forgotten',
        user_id=1,
        artist_id=10,
        song_url="https://yuhtube-bucket.s3.amazonaws.com/songs-seeds/MitiS+x+Crystal+Skies+-+Forgotten++Ophelia+Records.mp3",
        image_url="https://yuhtube-bucket.s3.amazonaws.com/album-seeds/lost-album.jpg",
        track_number=9,
        album_id=10
    ),
    Song( #107
        title='Running Away (feat. Ashley Apollodor)',
        user_id=1,
        artist_id=10,
        song_url="https://yuhtube-bucket.s3.amazonaws.com/songs-seeds/MitiS+x+SubLion+-+Running+Away+(feat.+Ashley+Apollodor)++Ophelia+Records.mp3",
        image_url="https://yuhtube-bucket.s3.amazonaws.com/album-seeds/lost-album.jpg",
        track_number=10,
        album_id=10
    ),
    Song( #108
        title='Back To Me (feat. Bella Renee)',
        user_id=1,
        artist_id=10,
        song_url="https://yuhtube-bucket.s3.amazonaws.com/songs-seeds/MitiS+-+Back+To+Me+(feat.+Bella+Renee)++Ophelia+Records.mp3",
        image_url="https://yuhtube-bucket.s3.amazonaws.com/album-seeds/lost-album.jpg",
        track_number=11,
        album_id=10
    ),
    Song( #109
        title='Found (Outro)',
        user_id=1,
        artist_id=10,
        song_url="https://yuhtube-bucket.s3.amazonaws.com/songs-seeds/MitiS+-+Found+(Outro)++Ophelia+Records.mp3",
        image_url="https://yuhtube-bucket.s3.amazonaws.com/album-seeds/lost-album.jpg",
        track_number=12,
        album_id=10
    ),
    Song( #110
        title='you were good to me',
        user_id=1,
        artist_id=11,
        song_url="https://yuhtube-bucket.s3.amazonaws.com/songs-seeds/Chelsea+Cutler+%26+Jeremy+Zucker+-+you+were+good+to+me+(Official+Audio).mp3",
        image_url="https://yuhtube-bucket.s3.amazonaws.com/album-seeds/brent-album.jpg",
        track_number=1,
        album_id=11
    ),
    Song( #111
        title='please',
        user_id=1,
        artist_id=11,
        song_url="https://yuhtube-bucket.s3.amazonaws.com/songs-seeds/Chelsea+Cutler%2C+Jeremy+Zucker+-+please+(Official+Audio).mp3",
        image_url="https://yuhtube-bucket.s3.amazonaws.com/album-seeds/brent-album.jpg",
        track_number=2,
        album_id=11
    ),
    Song( #112
        title='sometimes',
        user_id=1,
        artist_id=11,
        song_url="https://yuhtube-bucket.s3.amazonaws.com/songs-seeds/Chelsea+Cutler+-+Sometimes+(Official+Audio).mp3",
        image_url="https://yuhtube-bucket.s3.amazonaws.com/album-seeds/brent-album.jpg",
        track_number=3,
        album_id=11
    ),
    Song( #113
        title='hello old friend',
        user_id=1,
        artist_id=11,
        song_url="https://yuhtube-bucket.s3.amazonaws.com/songs-seeds/Jeremy+Zucker%2C+Chelsea+Cutler+-+hello+old+friend+(Official+Audio).mp3",
        image_url="https://yuhtube-bucket.s3.amazonaws.com/album-seeds/brent-album.jpg",
        track_number=4,
        album_id=11
    ),
    Song( #114
        title='scared',
        user_id=1,
        artist_id=11,
        song_url="https://yuhtube-bucket.s3.amazonaws.com/songs-seeds/Chelsea+Cutler+%26+Jeremy+Zucker+-+Scared+(Official+Audio).mp3",
        image_url="https://yuhtube-bucket.s3.amazonaws.com/album-seeds/brent-album.jpg",
        track_number=5,
        album_id=11
    ),
    Song( #115
        title='FML',
        user_id=1,
        artist_id=12,
        song_url="https://yuhtube-bucket.s3.amazonaws.com/songs-seeds/Deadmau5+-+FML++HD.mp3",
        image_url="https://yuhtube-bucket.s3.amazonaws.com/album-seeds/forlackofabettername-album.jpg",
        track_number=1,
        album_id=12
    ),
    Song( #116
        title='Moar Ghosts n Stuff',
        user_id=1,
        artist_id=12,
        song_url="https://yuhtube-bucket.s3.amazonaws.com/songs-seeds/Deadmau5+-+Moar+Ghosts+'n'+Stuff.mp3",
        image_url="https://yuhtube-bucket.s3.amazonaws.com/album-seeds/forlackofabettername-album.jpg",
        track_number=2,
        album_id=12
    ),
    Song( #117
        title="Ghosts 'n' Stuff (feat. Rob Swire)",
        user_id=1,
        artist_id=12,
        song_url="https://yuhtube-bucket.s3.amazonaws.com/songs-seeds/Deadmau5+-+Ghosts+'n'+Stuff.mp3",
        image_url="https://yuhtube-bucket.s3.amazonaws.com/album-seeds/forlackofabettername-album.jpg",
        track_number=3,
        album_id=12
    ),
    Song( #118
        title="Hi Friend!",
        user_id=1,
        artist_id=12,
        song_url="https://yuhtube-bucket.s3.amazonaws.com/songs-seeds/Deadmau5+-+Hi+Friend.mp3",
        image_url="https://yuhtube-bucket.s3.amazonaws.com/album-seeds/forlackofabettername-album.jpg",
        track_number=4,
        album_id=12
    ),
      Song( #119
        title='Bot',
        user_id=1,
        artist_id=12,
        song_url="https://yuhtube-bucket.s3.amazonaws.com/songs-seeds/Deadmau5+-+Bot.mp3",
        image_url="https://yuhtube-bucket.s3.amazonaws.com/album-seeds/forlackofabettername-album.jpg",
        track_number=5,
        album_id=12
    ),
      Song( #120
        title='Word Problems',
        user_id=1,
        artist_id=12,
        song_url="https://yuhtube-bucket.s3.amazonaws.com/songs-seeds/deadmau5+-+Word+Problems+(audio).mp3",
        image_url="https://yuhtube-bucket.s3.amazonaws.com/album-seeds/forlackofabettername-album.jpg",
        track_number=6,
        album_id=12
    ),
      Song( #121
        title='Soma',
        user_id=1,
        artist_id=12,
        song_url="https://yuhtube-bucket.s3.amazonaws.com/songs-seeds/Deadmau5+-+Soma++HD.mp3",
        image_url="https://yuhtube-bucket.s3.amazonaws.com/album-seeds/forlackofabettername-album.jpg",
        track_number=7,
        album_id=12
    ),
      Song( #122
        title='Lack Of A Better Name',
        user_id=1,
        artist_id=12,
        song_url="https://yuhtube-bucket.s3.amazonaws.com/songs-seeds/Deadmau5+-+Lack+of+a+Better+Name+(1080p)++HD.mp3",
        image_url="https://yuhtube-bucket.s3.amazonaws.com/album-seeds/forlackofabettername-album.jpg",
        track_number=8,
        album_id=12
    ),
      Song( #123
        title='The 16th Hour',
        user_id=1,
        artist_id=12,
        song_url="https://yuhtube-bucket.s3.amazonaws.com/songs-seeds/Deadmau5+-+The+16th+Hour++HD.mp3",
        image_url="https://yuhtube-bucket.s3.amazonaws.com/album-seeds/forlackofabettername-album.jpg",
        track_number=9,
        album_id=12
    ),
      Song( #124
        title='Strobe',
        user_id=1,
        artist_id=12,
        song_url="https://yuhtube-bucket.s3.amazonaws.com/songs-seeds/deadmau5+-+Strobe.mp3",
        image_url="https://yuhtube-bucket.s3.amazonaws.com/album-seeds/forlackofabettername-album.jpg",
        track_number=10,
        album_id=12
    ),
]

def seed_songs():
    for song in songs:
        db.session.add(song)

        add_likes_to_songs(song)

    db.session.commit()


def undo_songs():
    db.session.execute('TRUNCATE songs RESTART IDENTITY CASCADE;')
    db.session.commit()
