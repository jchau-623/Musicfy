import React, { useEffect, useState } from 'react';
import { NavLink } from 'react-router-dom';
import { useSelector } from 'react-redux';
import LogoutButton from '../auth/LogoutButton';

import './NavBar.css'

export default function NavBar() {
  const user = useSelector(({ session }) => session.user);
  const body = document.querySelector('body')
  body.style.margin = '0'

  const [isHomePage, setIsHomePage] = useState(false);
  const [isLibraryPage, setIsLibraryPage] = useState(false)

  useEffect(() => {
    if (window.location.href === 'http://localhost:3000/') {
      setIsHomePage(true)
    } else {
      setIsHomePage(false)
    }
  }, []);

  useEffect(() => {
    if (window.location.href === 'http://localhost:3000/library') {
      setIsLibraryPage(true)
    } else {
      setIsLibraryPage(false)
    }
  }, []);

  return (
    <div className='nav-bar'>
      <div className='leftnav-tophalf'>
        <NavLink to='/' exact={true} activeClassName='active' className='navlink'>
          <div className={`leftnav-tab ${isHomePage ? 'highlighted' : ''}`} >
            <i className="fa-solid fa-house" />
            Home
          </div>
        </NavLink>
        <NavLink to='/library' exact={true} activeClassName='active' className='navlink'>
          <div className={`leftnav-tab ${isLibraryPage ? 'highlighted' : ''}`} >
          <i className="fa-solid fa-book" />
            Your Library
          </div>
        </NavLink>
      <LogoutButton />
      </div>
      <div className='leftnav-bothalf'>

      </div>
    </div>
  );
}
