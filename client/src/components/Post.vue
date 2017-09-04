<template>
  <div id="app">

     <!-- Post Content -->
     <article>
       <div class="container">
         <div v-if="post" class="row">
             <div class="col-12 p-4">
               <h1 class>{{ post.title }}</h1>
               <i class='meta'>
                 Posted by Ben Patterson on {{post.created}}
               </i>
             </div>
            <div v-html="post.entry" class="col-12 px-4"></div>
         </div>
       </div>
     </article>
   </div>
</template>

<script>
  export default {
    name: 'entry',
    created () {
      return this.loadPost()
    },
    computed: {
      post () {
        let id = this.$route.params.id
        return this.$store.state.posts[id]
      }
    },
    methods: {
      loadPost () {
        return this.$store.dispatch('FETCH_POST')
      }
    }
  }
</script>

<style scoped=""lang="sass">
    @import "src/assets/styles/blog/clean-blog";
</style>