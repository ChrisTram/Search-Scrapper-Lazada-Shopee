import React, { Component } from 'react';
import { NavLink } from 'react-router-dom';
import { Navbar, Nav } from 'react-bootstrap';

export class Navigation extends Component {

    render() {
        return (
            <Navbar bg="dark" variant="dark">
              <Nav className="me-auto">
                <Nav.Link href="/products">Home</Nav.Link>
                <Nav.Link href="#">Search</Nav.Link>
              </Nav>
          </Navbar>
            
        )
    }
}