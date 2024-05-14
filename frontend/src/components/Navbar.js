import React, { useState } from 'react'
import { Button } from './Button'
import { Link } from 'react-router-dom'
import './Navbar.css'
import Dropdown from './Dropdown'

function Navbar() {
    const [click, setClick] = useState(false)
    const [dropdown, setDropdown] = useState(false)

    const handleClick = () => setClick(!click);
    const closeMobileMenu = () => setClick(false);
    return (
        <>
            <nav className='navbar'>
                <Link to='/' className='navbar-logo'>
                    JolsAid
                </Link>
                <div className='menu-icon' onClick={handleClick}>
                    <i className={click ? 'fas fa-times' : 'fas fa-bars'} />
                </div>
                <ul className={click ? 'nav-menu active' : 'nav-menu'}>
                    <li className='nav-item'>
                        <Link to='/' className='nav-links' onClick={closeMobileMenu}>
                            Deals <i className='fas fa-caret-down' />
                        </Link>
                        {dropdown && <Dropdown />}
                    </li>
                    <li className='nav-item'>
                        <Link to='/deals' className='nav-links'>
                            Deals
                        </Link>
                    </li>
                    <li className='nav-item'>
                        <Link to='/categories' className='nav-links'>
                            Category
                        </Link>
                    </li>
                    <li className='nav-item'>
                        <Link to='/brands' className='nav-links'>
                            Brand
                        </Link>
                    </li>
                    <li className='nav-item'>
                        <Link to='/sign-up' className='nav-links-mobile'>
                            Sign Up
                        </Link>
                    </li>
                </ul>
            </nav>
        </>
    )