import React, { useEffect, useState } from 'react';
import { useDispatch, useSelector } from 'react-redux'
import SongPlayer from '../SongPlayer';
import AlbumPlayer from '../AlbumPlayer';
import HomeSidebar from './HomeSidebar';
import MainSidebar from '../MainSidebar';
import TileCarousel from '../TileCarousel';
import { getNewAlbumsArray, getNewSongsArray, getTopAlbumsArray, loadHome, setLoaded } from '../../store/home';
import { getPlaylists } from '../../store/playlists';
import './HomePage.css'
// import Album from './Album';

export default function HomePage() {

    const dispatch = useDispatch();

    const [homeDisplay, setHomeDisplay] = useState('albums');
    const homeItems = useSelector(({ home }) => home);
    const newSongs = useSelector(getNewSongsArray);
    const newAlbums = useSelector(getNewAlbumsArray);
    const featuredAlbum = homeItems.featuredAlbum;
    const featuredSongs = Object.values(homeItems.featuredSongs)
    const topAlbums = useSelector(getTopAlbumsArray);


    useEffect(() => {
        if (homeItems.isLoaded) return;
        dispatch(getPlaylists());
        dispatch(loadHome());
        dispatch(setLoaded());
    }, [dispatch, homeItems])

    let homeContent;
    if (homeDisplay === 'albums') {
        homeContent = (
            <>
                <h2>Featured Album</h2>
                <AlbumPlayer album={featuredAlbum} />

                <h2>New Albums</h2>
                <TileCarousel content={newAlbums} option='albums' identifier='newAlbums'/>

                <h2>Top Albums</h2>
                <TileCarousel content={topAlbums} option='albums'identifier='topAlbums'/>
            </>
        )
    } else if (homeDisplay === 'songs') {
        homeContent = (
            <>
                <h2>Featured Songs</h2>
                <div className='featured-songs-container'>
                    {featuredSongs.map((song, idx) => (
                        <SongPlayer key={idx} song={song}/>

                    ))}
                </div>
                <h2>New Songs</h2>
                <TileCarousel content={newSongs} option='songs'/>
            </>
        )
    }

    return (
        <div id='home-wrapper'>
            <div className='main-wrapper'>
                {homeContent}
            </div>

            <div className='sidebar-container'>
                <MainSidebar />

                <HomeSidebar setHomeDisplay={setHomeDisplay} homeDisplay={homeDisplay}/>
            </div>
        </div>
    )
};
