import React, { Component } from 'react';
import 'request'

import { Col } from 'react-bootstrap';
class Main extends Component {
  render() {
    return (
      <Col mdOffset={2} xs={12} md={8} >

       <div className="row">
         <form action='http://localhost:8080/api/entry' method='post' >
           <input type='text' name='title' value={ JSON.stringify(process.env) }></input>
           <input type='textbox' name='entry'></input>
           <button type='submit'>Post Blog</button>
         </form>
       </div>
      </Col>
    );
  }
}

export default Main;
