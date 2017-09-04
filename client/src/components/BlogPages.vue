<template>
    <div id="app">
      <div class="row">
        <div class="col-lg-8 col-md-10 mx-auto">
          <div v-for="entry in posts" class="px-4" >
            <router-link
              :to="{ name: 'post', params: { id: entry.id } }"
              class="post-preview"
             >
              <h2 class="post-title">
                {{ entry.title }}
              </h2>
            </router-link>
            <i class="post-meta">Posted by
              <a href="#">Ben Patterson</a>
              on {{ entry.created }}</i>
          </div>
          <hr>
          <div class="clearfix">
              <router-link :to="{ name: 'offsetBlog', params: { page:previousPage } }" v-if="currentPage > 0">
                 <div class="btn btn-secondary float-left"  >Previous Posts &larr;</div>
             </router-link>
              <router-link :to="{ name: 'offsetBlog', params: { page:nextPage } }" v-if="hasMore">
                <div class="btn btn-secondary float-right" >Older Posts &rarr;</div>
              </router-link>
          </div>
        </div>
      </div>
    </div>
</template>

  <script>
  export default {
    name: 'pages',
    created () {
      return this.loadPosts()
    },
    computed: {
      posts () {
        let page = Number(this.$route.params.page || '0')
        return Object.values(this.$store.state.posts)
        .filter((post) => post.page === page)
        .sort((a, b) => b.timestamp - a.timestamp)
      },

      hasMore () {
        return (this.$store.state.posts.total - this.currentPage * 10) > 10
      },

      nextPage () {
        return this.currentPage + 1
      },

      previousPage () {
        return this.currentPage - 1
      },

      currentPage () {
        return Number(this.$route.params.page || '0')
      }
    },
    watch: {
      '$route': 'loadPosts'
    },
    methods: {
      loadPosts () {
        return this.$store.dispatch('FETCH_ENTRY_DATA')
      }
    }
  }
  </script>
  <style scoped lang="sass">
      @import "src/assets/styles/blog/clean-blog";
  </style>