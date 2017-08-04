import React, { Component } from 'react';
import { Col } from 'react-bootstrap';
import * as BlogActions from "../actions/BlogActions";
import { Link } from 'react-router-dom';
import BlogStore from "../stores/BlogStore";
import { markdown } from 'markdown';

export default class Blog extends Component {
  constructor({ match }) {
  super();
    this.state = {
      offset: match.params &&  parseInt(match.params.offset) || 0,
      entries: BlogStore.getAll(),
    };
    this.getEntries = this.getEntries.bind(this);
    this.setOffset = this.setOffset.bind(this);
  }
  componentWillMount() {
    BlogActions.getEntries(this.state.offset);
    BlogStore.on("change", this.getEntries);
  }

  componentWillUnmount() {
    BlogStore.removeListener("change", this.getEntries);
  }

  getEntries() {
    this.setState({
      offset: this.state.offset,
      entries: BlogStore.getAll(),
    });
  }

  setOffset() {
    let offset = this.state.offset + 10;
    BlogActions.getEntries(offset);
    this.setState({
      offset:offset,
      entries: BlogStore.getAll(),
    });
  }


  renderEntry(entry) {
    return { __html: markdown.toHTML(entry.entry) };
  }


  render() {
    const { entries, offset } = this.state;
    var nextOffset = parseInt(this.offset) + 10;
    const EntryComponents = entries.map((entry)=>{
      var link = "/blog/entry/" + entry.id;
      var getEntry = function(){ BlogActions.getEntry(entry.id); };
      return <li key={entry.id}>
           <Link to={link} onClick={getEntry}><ul>
             <li>{entry.created}</li>
             <li>{entry.title}</li>
           </ul>
         </Link>
        </li>
    })
    var next = entries.length == 10 ? 
      <Link to={'/blogs/' + (offset +10)} onClick={this.setOffset}> next</Link> :
        <div></div>
    return (
      <Col mdOffset={2} xs={12} md={8} >
         <ul>{ EntryComponents } </ul>
          { next }

      </Col>
    );
  }
}

