import React, { Component } from 'react';
import { Nav, NavItem, Navbar } from 'react-bootstrap';
import { Link } from 'react-router-dom'
export default class NavbarInstance extends Component{
  render(){
    return (
      <Navbar inverse collapseOnSelect >
        <Navbar.Header>
          <Navbar.Brand>
            <Link to="/">Home</Link>
           </Navbar.Brand>
           <Navbar.Toggle />
        </Navbar.Header>

        <Navbar.Collapse>
          <Nav>
            <NavItem eventKey={2} href="/portfolio"><Link to="portfolio" >Portfolio</Link></NavItem>
            <NavItem eventKey={2} href="/contact"><Link to="/contact">Contact</Link></NavItem>
            <NavItem eventKey={2} href="/blog"><Link to="/blog">Blog</Link></NavItem>
          </Nav>
        </Navbar.Collapse>
      </Navbar>
    );
  }
}