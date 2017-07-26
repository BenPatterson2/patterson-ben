import React, { Component } from 'react';
import { Col, Image } from 'react-bootstrap';
import profile_photo from '../imgs/profile-photo.jpg';
export default class Home extends Component {
  render() {
    return (
      <div>
      <Col xsOffset={1} xs={10} md={4}>
        <Image src={profile_photo} circle responsive/>
      </Col>

      <Col xsOffset={1} mdOffset={2} xs={10} md={3} >
       <div className="row st-padding">
          <p> I'm a programmer, serial meetup joiner, life-long learner, runner, etc.. Sometimes, I'll write a blog entry.</p>
       </div>

      </Col>
    </div>
    );
  }
}

