import dispatcher from "../dispatcher";
import request from "request-promise-native";



export function getEntries(offset) {
  dispatcher.dispatch({type: "FETCH_ENTRIES"});
  request.get({url:`https://patterson-ben.appspot.com/api/entries?offset=${offset}`,json:true})
  .then((response)=>{
    dispatcher.dispatch({type: "RECEIVE_ENTRIES", entries: response.entries });
  });
}

export function getEntry(id) {
  dispatcher.dispatch({type: "FETCH_ENTRY"});
  request.get({url:`https://patterson-ben.appspot.com/api/entry/` + id, json:true})
  .then((response) =>{
    dispatcher.dispatch({type: "RECEIVE_ENTRY", entry: response });
  });
}
