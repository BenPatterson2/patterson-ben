import dispatcher from "../dispatcher";
import request from "reaquest-promise-native";

export function createTodo(id) {
  dispatcher.dispatch({
    type: "CREATE_TODO",
    text,
  });
}



export function reloadTodos() {
  dispatcher.dispatch({type: "FETCH_ENTRIES"});
  var myInit = { method: 'GET',
               mode: 'cors',
             }
  request.get({url:"https://patterson-ben.appspot.com/api/blog",json:true})
  .then((response)=>{
    console.log(response);
    dispatcher.dispatch({type: "RECIEVE_ENTRIES", payload: response.json });
  });
}
