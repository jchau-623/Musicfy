
import React from 'react';
import { NavLink } from 'react-router-dom';
import LogoutButton from '../auth/LogoutButton';
import './NavBar.css'

export default function NavBar() {
  return (
    <nav className='nav-bar'>
      <div>
          <LogoutButton />
      </div>

    </nav>
  );
}
