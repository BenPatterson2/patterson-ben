import React, { Component } from 'react';
import { Col } from 'react-bootstrap';
import * as BlogActions from "../actions/BlogActions";
import BlogStore from "../stores/BlogStore";
import { markdown } from 'markdown';

export default class BlogEntry extends Component {
  constructor({ match }) {
  super();
    this.id = match.params.id;
    this.getEntry = this.getEntry.bind(this);
    BlogActions.getEntry(this.id);
    this.state = {
      entry: BlogStore.getEntry()
    };
  }

  componentWillMount() {
    BlogStore.on("change", this.getEntry);
  }

  componentWillUnmount() {
    BlogStore.removeListener("change", this.getEntry);
  }

  getEntry(){
    this.setState({
      entry: BlogStore.getEntry(),
    })
  }

  renderEntry(entry) {
    return { __html: markdown.toHTML(entry.entry) };
  }


  render() {
    return (
      <Col mdOffset={2} xs={12} md={8} >
           <h4>{this.state.entry.title}</h4>
          <div dangerouslySetInnerHTML={ this.renderEntry(this.state.entry) }></div>
      </Col>
    );
  }
}

