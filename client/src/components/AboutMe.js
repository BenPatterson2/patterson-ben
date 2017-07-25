import React, { Component } from 'react';
import { Col } from 'react-bootstrap';
class AboutMe extends Component {
  render() {
    return (
      <Col mdOffset={2} xs={12} md={8} >

       <div className="row">
        <p>
         I'm a Seattle-based programmer. Likes writing test learning new things, refactoring code.  I've written
         software for Xtramath.com and stuffmapper.com. Strong believer that writing good tests is a part of writing good software.
         I'm on github as <a href="https://github.com/BenRuns">BenRuns</a>.
         <p>
           
         </p>
         Other than programming, I also enjoy
          long distance running, drinking coffee, collecting Gundam models and spending time with family. There may or may not be blog entries related to those things on this site
        </p>

       </div>

      </Col>
    );
  }
}

export default AboutMe;
