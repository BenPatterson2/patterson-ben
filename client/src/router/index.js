import Vue from 'vue'
import Router from 'vue-router'
import Home from '@/views/Home'
import Blog from '@/views/Blog'
import Post from '@/components/Post'
import BlogPages from '@/components/BlogPages'

Vue.use(Router)

export function createRouter () {
  return new Router({
    routes: [
      {
        path: '/',
        name: 'home',
        component: Home
      },
      {
        path: '/blog',
        component: Blog,
        children: [
          {
            path: '/',
            name: 'blog',
            component: BlogPages
          },
          {
            name: 'offsetBlog',
            path: ':page',
            component: BlogPages
          },
          {
            path: 'post/:id',
            name: 'post',
            component: Post
          }
        ]
      }
    ]
  })
}
