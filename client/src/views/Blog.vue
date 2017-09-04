<template>

    <div id="app">

      <!-- Navigation -->
      <b-navbar toggleable="md" class="navbar-light fixed-top" id="mainNav">
        <div class="container">
          <b-navbar-brand href="/">Ben Patterson</b-navbar-brand>

          <b-nav-toggle right target="nav_collapse">
            Menu
            <i class="fa fa-bars"></i>
          </b-nav-toggle>

          <b-collapse right is-nav id="nav_collapse">
            <b-nav is-nav-bar class="ml-auto">
              <b-nav-item>
                <router-link class='nav-link' to='/blog'>Home</router-link>
              </b-nav-item>
              <b-nav-item>
                <router-link class='nav-link' to='/'>About</router-link>
              </b-nav-item>

            </b-nav>
          </b-collapse>
        </div>
      </b-navbar>

      <!-- Page Header -->
      <header class="masthead" :style="{ backgroundImage: `url('${require('../assets/img/home-bg.jpg')}')` }">
        <div class="container">
          <div class="row">
            <div class="col-lg-8 col-md-10 mx-auto">
              <div class="site-heading">
                <h1>Keeping Up</h1>
                <span class="subheading">A tech blog with occasional posts about running</span>
              </div>
            </div>
          </div>
        </div>
      </header>

      <!-- Main Content -->
      <router-view></router-view>

      <hr>

      <!-- Footer -->
      <footer>
        <div class="container">
          <div class="row">
            <div class="col-lg-8 col-md-10 mx-auto">
              <ul class="list-inline text-center">
                <li class="list-inline-item">
                  <a href="https://twitter.com/benruns">
                    <span class="fa-stack fa-lg">
                      <i class="fa fa-circle fa-stack-2x"></i>
                      <i class="fa fa-twitter fa-stack-1x fa-inverse"></i>
                    </span>
                  </a>
                </li>

                <li class="list-inline-item">
                  <a href="https://github.com/BenRuns">
                    <span class="fa-stack fa-lg">
                      <i class="fa fa-circle fa-stack-2x"></i>
                      <i class="fa fa-github fa-stack-1x fa-inverse"></i>
                    </span>
                  </a>
                </li>
              </ul>
              <p class="copyright text-muted">Copyright &copy; Ben Patterson 2017</p>
            </div>
          </div>
        </div>
      </footer>
    </div>
</template>

  <script>
  export default {
    name: 'blog'
  }
  </script>
  <style scoped lang="sass">
    @import "src/assets/styles/blog/clean-blog";

  </style>