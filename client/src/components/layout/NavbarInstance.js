import React, { Component } from 'react';
import { Nav, NavItem, Navbar } from 'react-bootstrap';
import { NavLink } from 'react-router-dom';
export default class NavbarInstance extends Component{
  render(){
    return (
      <Navbar inverse collapseOnSelect >
        <Navbar.Header>
          <Navbar.Brand>
            <NavLink to="/">Home</NavLink>
           </Navbar.Brand>
           <Navbar.Toggle />
        </Navbar.Header>

        <Navbar.Collapse>
          <Nav>
            <NavItem eventKey={2} href="#"><NavLink to="/portfolio" >Portfolio</NavLink></NavItem>
            <NavItem eventKey={2} href="#"><NavLink to="/contact">Contact</NavLink></NavItem>

            <NavItem eventKey={2} href="#"><NavLink to="/blog">Blog</NavLink></NavItem>
          </Nav>
        </Navbar.Collapse>
      </Navbar>
    );
  }
}