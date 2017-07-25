import React, { Component } from 'react';
import { Col } from 'react-bootstrap';

export default class Contact extends Component {
  render() {
    return (
        <Col mdOffset={2} xs={12} md={8} >

          <a href="mailto:Ben@benpatterson.io">Ben@benpatterson.io </a>  or
            <a href="tel:763-268-9235" > 763-268-9235 </a>
      </Col>
    );
  }
}

