const API_URL = window.location.origin + '/api'
export default {
  FETCH_POST: ({ commit, dispatch, state }) => {
    let id = state.route.params.id
    var request = new Request(`${API_URL}/entry/${id}`, {
      headers: new Headers({ 'Content-Type': 'application/json', 'Access-Control-Allow-Origin': '*' })
    })
    return fetch(request, { mode: 'cors', credentials: 'include' })
      .then((data) => {
        return data.json().then(json => {
          commit('SET_ENTRY', json)
        })
      })
  },
  // ensure data for rendering given list type
  FETCH_ENTRY_DATA: ({ commit, dispatch, state }) => {
    // commit('SET_ACTIVE_TYPE', { type })
    let offset = Number(state.route.params.page || '0') * 10
    var request = new Request(`${API_URL}/entries?offset=${offset}`, {
      headers: new Headers({ 'Content-Type': 'application/json', 'Access-Control-Allow-Origin': '*' })
    })
    return fetch(request, { mode: 'cors', credentials: 'include' })
      .then((data) => {
        return data.json().then(json => {
          console.log(json, 'line 25')
          commit('SET_ENTRY_LIST', json)
        })
      })
  }
}

