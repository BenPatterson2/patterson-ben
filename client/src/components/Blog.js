import React, { Component } from 'react';
import { Col } from 'react-bootstrap';
export default class Blog extends Component {
  render() {
    return (
      <Col mdOffset={1} xs={12} md={10} >
        I'm currently messing around with React.js and Flask. Hope to get a blog post about this up soon.
      </Col>
    );
  }
}

