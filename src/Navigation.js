import React, { Component } from 'react';
import { Link, NavLink } from 'react-router-dom';
import { Navbar, Nav } from 'react-bootstrap';

export class Navigation extends Component {

    render() {
        return (
            <Navbar bg="dark" variant="dark">
              <Nav className="me-auto">
                <Nav.Link as={Link} to="/products">Products</Nav.Link>
              </Nav>
          </Navbar>
            
        )
    }
}