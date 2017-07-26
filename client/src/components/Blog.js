import React, { Component } from 'react';
import { Col } from 'react-bootstrap';

export default class Blog extends Component {
  render() {
    return (
        <Col mdOffset={2} xs={12} md={8} >
          <p>I swear that the blog will return.
             Potential employers! If you want my opinion on someting in a long format, send me an email with a request.
             Getting the blog back up will magically rise to the top of my priority list.
           </p>
      </Col>
    );
  }
}

