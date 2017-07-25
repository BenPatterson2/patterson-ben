import AboutMe from './components/AboutMe';
import Blog from './components/Blog';
import Contact from './components/Contact';
import Layout from './layout/Layout'
import React from 'react';
import ReactDOM from 'react-dom';



import {
  BrowserRouter as Router,
  Route
} from 'react-router-dom'

import { Row } from 'react-bootstrap';
import './index.css';

const app =  document.getElementById('root')
ReactDOM.render(
  <Router>
    <Layout>
        <Route exact path="/" component={AboutMe}/>
        <Route path="/blog" component={Blog}/>
        <Route path="/about-me" component={AboutMe}></Route>
        <Route path="/contact" component={Contact}></Route>
    </Layout>
  </Router>,
 app
);

