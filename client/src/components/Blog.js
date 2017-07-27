import React, { Component } from 'react';
import { Col } from 'react-bootstrap';
import * as BlogActions from "../actions/BlogActions";
import BlogStore from "../stores/BlogStore";
import { markdown } from 'markdown';

export default class Blog extends Component {
  constructor() {
  super();
    this.getEntries = this.getEntries.bind(this);
    BlogActions.getEntries();
    this.state = {
      entries: BlogStore.getAll(),
    };
  }
  componentWillMount() {
    BlogStore.on("change", this.getEntries);
  }

  componentWillUnmount() {
    BlogStore.removeListener("change", this.getEntries);
  }

  getEntries() {
    this.setState({
      entries: BlogStore.getAll(),
    })
  }

  renderEntry(entry) {
    return { __html: markdown.toHTML(entry.entry) };
  }


  render() {
    const { entries } = this.state;
    const EntryComponents = entries.map((entry)=>{
      return <li key={entry.id}>
           <ul>
             <li>{entry.created}</li>
             <li>{entry.title}</li>
             <li dangerouslySetInnerHTML={ this.renderEntry(entry) }></li>
          </ul>
        </li>
    })
    return (
      <Col mdOffset={2} xs={12} md={8} >
         <p> Well, I can access my old entries but styling, pagination, creation and editing will have to wait. Still getting used to react patterns.</p>
         <ul>{ EntryComponents } </ul>
      </Col>
    );
  }
}

