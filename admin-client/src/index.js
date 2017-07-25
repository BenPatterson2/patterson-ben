import Main from './components/Main';
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
        <Route exact path="/" component={Main}/>
    </Layout>
  </Router>,
 app
);
