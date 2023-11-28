import React, { useEffect, useState } from 'react';
import { useDispatch, useSelector } from 'react-redux'
import NavBar from '../NavBar';
import './YourLibraryPage.css'

export default function YourLibraryPage() {

    const dispatch = useDispatch()

    return (
        <div className='page-container'>
            <NavBar />
            <div className='page-content'>
                <h1>Your Library Page</h1>
            </div>
        </div>

    )
}
