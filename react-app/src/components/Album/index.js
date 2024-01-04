import React from 'react';

const Album = ({ album, onClick }) => {
    return (
        <div className='album' onClick={onClick}>
            <img src={album.coverImageUrl} alt={album.title} />
            <h3>{album.title}</h3>
            <p>{album.artist}</p>
            {/* Add additional album details as needed */}
        </div>
    );
}; 

export default Album;
