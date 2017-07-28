import { EventEmitter } from "events";

import dispatcher from "../dispatcher";

class BlogStore extends EventEmitter {
  constructor() {
    super();
    this.entries = [];
    this.entry = { title:'loading', entry:'loading', id:'loading' };
  }

  getAll() {
    return this.entries;
  }
  getEntry(){
    return this.entry;
  }

  handleActions(action) {
    switch(action.type) {

      case "RECEIVE_ENTRIES": {
        this.entries = action.entries;
        this.emit("change");
        break;
      }

      case "RECEIVE_ENTRY": {
        this.entry = action.entry;
        this.emit("change");
        break;
      }
    }
  }

}

const blogStore = new BlogStore();
dispatcher.register(blogStore.handleActions.bind(blogStore));

export default blogStore;
