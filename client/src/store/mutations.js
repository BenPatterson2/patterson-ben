import Vue from 'vue'
export default {

  SET_ENTRY: (state, post) => {
    Vue.set(state.posts, post.id, post)
  },

  SET_ENTRY_LIST: (state, { total, posts }) => {
    let page = Number(state.route.params.page || '0')
    state.posts.total = total
    posts.forEach(post => {
      post.page = page
      Vue.set(state.posts, post.id, post)
    })
  }
}
