import request from "request";

export function fetchTweets() {
  return function(dispatch) {
    axios.get("http://rest.learncode.academy/api/test123/tweets")
      .then((response) => {
        dispatch({type: "FETCH_TWEETS_FULFILLED", payload: response.data})
      })
      .catch((err) => {
        dispatch({type: "FETCH_TWEETS_REJECTED", payload: err})
      })
  }
}

export function fetchEntries() {
  return function(dispatch) {
    request.post("http://rest.learncode.academy/api/test123/tweets")
      .then((response) => {
        dispatch({type: "FETCH_TWEETS_FULFILLED", payload: response.data})
      })
      .catch((err) => {
        dispatch({type: "FETCH_TWEETS_REJECTED", payload: err})
      })
  }
}
