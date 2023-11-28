import React, { useState } from 'react';
import { useDispatch, useSelector } from 'react-redux';
import { loadSongAndSetQueue, setSong } from '../../store/active';
import { createSongLike, deleteSongLike } from '../../store/session';
import './SongPlayer.css';

export default function SongPlayer({ song }) {
    const dispatch = useDispatch();

    const playSong = (e) => {
        e.stopPropagation();
        dispatch(loadSongAndSetQueue(song));
    };

    return (
        <div
            className='song-player'
        >
            <div className='song-player-image-container'>
                <img
                    alt='featured song artwork'
                    className='song-player-image'
                    src={song.image_url}
                    onClick={playSong}
                />
            </div>
            <div className='song-player-overlay' onClick={playSong}>

                    <p className='song-title'>{song.title}</p>
                    <p className='song-artist'>{song.artist.name}</p>

            </div>
        </div>
    )
}
