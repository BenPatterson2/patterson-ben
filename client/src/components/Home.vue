<template>
  <div id="app">

    <!-- Navigation -->
    <nav class="navbar navbar-expand-lg navbar-light fixed-top" id="mainNav">
      <div class="container">
        <a class="navbar-brand js-scroll-trigger" href="/">Ben Patterson</a>
        <button class="navbar-toggler navbar-toggler-right" type="button" data-toggle="collapse" data-target="#navbarResponsive" aria-controls="navbarResponsive" aria-expanded="false" aria-label="Toggle navigation">
          Menu
          <i class="fa fa-bars"></i>
        </button>
        <div class="collapse navbar-collapse" id="navbarResponsive">
          <ul class="navbar-nav ml-auto">
            <!-- <li class="nav-item">
              <a class="nav-link js-scroll-trigger" href="#portfolio">Portfolio</a>
            </li> -->
            <!-- <li class="nav-item">
              <a class="nav-link js-scroll-trigger" href="#about">About</a>
            </li> -->
            <li class="nav-item">
              <router-link to='/blog'><a class="nav-link js-scroll-trigger" >Blog</a></router-link>
            </li>

            <!-- <li class="nav-item">
              <a class="nav-link js-scroll-trigger" href="#contact">Contact</a>
            </li> -->
          </ul>
        </div>
      </div>
    </nav>

    <!-- Header -->
    <header class="masthead">
      <div class="container">
        <img class="img-fluid" src="../assets/img/profile.png" alt="">
        <div class="intro-text">
          <span class="name">Ben Patterson</span>

          <ul class="list-inline">

            <li class="list-inline-item">
              <a class="btn-social btn-outline" href="https://github.com/BenRuns">
                <i class="fa fa-fw fa-github-alt"></i>
              </a>
            </li>
            <li class="list-inline-item">
              <a class="btn-social btn-outline" href="https://twitter.com/benruns">
                <i class="fa fa-fw fa-twitter"></i>
              </a>
            </li>
            <li class="list-inline-item">
              <a class="btn-social btn-outline" href="https://www.linkedin.com/in/bpatt1/">
                <i class="fa fa-fw fa-linkedin"></i>
              </a>
            </li>
            <li class="list-inline-item">
              <a class="btn-social btn-outline" href="mailto:ben@benpatterson.io">
                <i class="fa fa-fw fa-envelope"></i>
              </a>
            </li>
          </ul>
          <span class="skills">Software Developer - Father - Runner - Seattle, WA </span>
        </div>
      </div>
    </header>


    <!-- About Section -->
    <section class="success" id="about">
      <div class="container">
        <h2 class="text-center">About</h2>
        <hr class="star-light">
        <div class="row text-left">
          <div class="col-lg-4 ml-auto">
            <p>
              I started my journey into software in 2012 when the MIT began offering
              a version of it's Intro to Computer Science course on edx.org. I caught the bug and
              studied whenever I had free time. It was difficult path to do it on my own but, I
              eventually started working in the industry.I love the challenge of a
              good problem and the satisfaction you get from solving it.
            </p>
            <p>
              An unusual fact about me is that I'm very interested in testing software. It's odd
              that a self-taught developer has this focus. I’m drawn to the complexities of a good
              CI/CD pipeline and it’s promise of delivering higher quality working code.
            </p>
          </div>
          <div class="col-lg-4 mr-auto">
            <p>
              I put a lot of deliberate effort into keeping up on new technologies and
              improving my base skillset. If I notice that a lack of understanding or a
              habit is slowing me down, I'll dig down and work on it until it's no
              longer an issue.
            </p>
            <p>
              If I'm not programming, you'll probably find me out for a run,
              spending time with my daughter or studying something online. Work-life
              balance is important to me.
            </p>
          </div>
        </div>
      </div>
    </section>

    <!-- Contact Section -->
    <section id="contact">
      <div class="container">
        <h2 class="text-center">Contact Me</h2>
        <hr class="star-primary">
        <div class="row">
          <div class="col-lg-8 mx-auto">
            <p> <strong>Email:</strong> <a href="mailto:ben@benpatterson.io">ben@benpatterson.io</a> </p>
            <p> <strong>Phone:</strong>  763-268-9235 </p>
          </div>
        </div>
      </div>
    </section>

    <!-- Footer -->
    <footer class="text-center">
      <div class="footer-below">
        <div class="container">
          <div class="row">
            <div class="col-lg-12">
              Copyright &copy; Ben Patterson 2017
            </div>
          </div>
        </div>
      </div>
    </footer>

    <!-- Scroll to Top Button (Only visible on small and extra-small screen sizes) -->
    <div class="scroll-top d-lg-none">
      <a class="btn btn-primary js-scroll-trigger" href="#page-top">
        <i class="fa fa-chevron-up"></i>
      </a>
    </div>


    <!-- Bootstrap core JavaScript -->
    <!-- <script src="/static/vendor/jquery/jquery.min.js"></script>
    <script src="/static/vendor/popper/popper.min.js"></script>
    <script src="/static/vendor/bootstrap/js/bootstrap.min.js"></script> -->

    <!-- Plugin JavaScript -->
    <!-- <script src="/static/vendor/jquery-easing/jquery.easing.min.js"></script> -->

    <!-- Contact Form JavaScript -->
    <!-- <script src="/static/js/jqBootstrapValidation.min.js"></script>
    <script src="/static/js/contact_me.min.js"></script> -->

    <!-- Custom scripts for this template -->
    <!-- <script src="/static/js/scripts.min.js"></script> -->


  </div>
  </template>

  <script>
  export default {
    name: 'home'
  }
  </script>
  <style lang="sass">
    @import "src/assets/styles/home/freelancer";

  </style>