import React from "react";

import Todo from "../components/Todo";
import * as TodoActions from "../actions/BlogActions";
import BlogStore from "../stores/BlogStore";


export default class Blogs extends React.Component {
  constructor() {
    super();
    this.getBlogs = this.getBlog.bind(this);
    this.state = {
      entries: BlogStore.getAll(),
    };
  }

  componentWillMount() {
    BlogStore.on("change", this.getTodos);
  }

  componentWillUnmount() {
    BlogStore.removeListener("change", this.getTodos);
  }

  getTodos(offset) {
    this.setState({
      entries: BlogStore.getAll(),
    });
  }

  render() {
    const { entries } = this.state;

    const TodoComponents = entries.map((todo) => {
        return <Entry key={todo.id} {...todo}/>;
    });

    return (
      <div>
        <button onClick={this.reloadTodos.bind(this)}>Reload!</button>
        <h1>Todos</h1>
        <ul>{TodoComponents}</ul>
      </div>
    );
  }
}
