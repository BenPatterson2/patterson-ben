import React, { Component } from 'react';
import { Col } from 'react-bootstrap';
export default class Portfolio extends Component {
  render() {
    return (
      <Col mdOffset={2} xs={12} md={3} >
        <ul>
          <li><a href="https://github.com/BenRuns">Github</a></li>
          <li><a href="https://www.npmjs.com/~benruns">npm packages</a></li>
          <li><a href="https://rubygems.org/profiles/BenRuns">Ruby gems</a></li>
          <li><a href="https://benruns.github.io/game_of_life_js/">Game of Life Solution</a></li>
          <li><a href="https://www.linkedin.com/in/bpatt1/">Linkedin</a></li>
        </ul>
      </Col>
    );
  }
}

