export default {

  // items that should be currently displayed.
  // this Array may not be fully fetched.
  activePosts (state, getters) {
    // let page = Number(state.route.params.page || 0)
    // console.log(state.posts.length)
    return state.posts
  }
}
