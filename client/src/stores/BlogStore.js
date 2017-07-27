import { EventEmitter } from "events";

import dispatcher from "../dispatcher";

class BlogStore extends EventEmitter {
  constructor() {
    super();
    this.entries = [];
  }

  getAll() {
    return this.entries;
  }

  handleActions(action) {
    switch(action.type) {
      case "RECEIVE_ENTRIES": {
        this.entries = action.entries;
        this.emit("change");
        break;
      }
    }
  }

}

const blogStore = new BlogStore();
dispatcher.register(blogStore.handleActions.bind(blogStore));

export default blogStore;
