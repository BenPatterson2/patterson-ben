import React, { Component } from 'react';
import { Col } from 'react-bootstrap';
class AboutMe extends Component {
  render() {
    return (
      <Col mdOffset={2} xs={12} md={8} >

       <div className="row">
          <p> I'm a West Seattle Based programmer. I'm looking for work so feel
             free to contact me if you're looking for a dev. Checkout my
             <a href="https://www.linkedin.com/in/bpatt1/linkedin"> Linkedin Page </a>
             while I'm using this site to experiment with React, Flask, and Google App Engine.</p>
       </div>

      </Col>
    );
  }
}

export default AboutMe;
