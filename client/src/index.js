import Home from './components/Home';
import Contact from './components/Contact';
import Blog from './components/Blog';
import BlogEntry from './components/BlogEntry';
import Portfolio from './components/Portfolio';
import Layout from './layout/Layout';
import React from 'react';
import ReactDOM from 'react-dom';



import {
  BrowserRouter as Router,
  Route
} from 'react-router-dom';

import { Row } from 'react-bootstrap';
import './index.css';

const app =  document.getElementById('root');
ReactDOM.render(
  <Router>
    <Layout>
        <Route exact path="/" component={Home}/>
        <Route path="/home" component={Home}></Route>
        <Route path="/blog/entry/:id" component={BlogEntry}></Route>
        <Route path="/blog" component={Blog}></Route>
        <Route path="/contact" component={Contact}></Route>
        <Route path="/portfolio" component={Portfolio}></Route>
    </Layout>
  </Router>,
 app
);

