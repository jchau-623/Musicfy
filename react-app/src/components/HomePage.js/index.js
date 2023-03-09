import React, { useEffect, useState } from 'react';
import { useDispatch, useSelector } from 'react-redux'
import NavBar from '../NavBar';
import './HomePage.css'

export default function HomePage() {

    const dispatch = useDispatch()


    return (
        
        <div className='page-container'>
            <NavBar />
            <div className='page-content'>
                <h1>Home Page</h1>
            </div>
        </div>

    )
}
