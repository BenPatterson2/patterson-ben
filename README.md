
# Benpatterson.io

## Requirements

- Google App Engine for Python
  - Ubuntu:  [https://cloud.google.com/sdk/docs/#deb](https://cloud.google.com/sdk/docs/#deb)
  - Mac: [https://cloud.google.com/sdk/docs/#mac](https://cloud.google.com/sdk/docs/#mac)
- [pip](http://pip.readthedocs.io/en/stable/)
- [Node.js](https://nodejs.org/en/)

### Building The Client

    cd client/
    npm install
    npm run build

## Run Locally

1. Clone the repo

        $ git clone git@github.com:BenRuns/patterson-ben.git

3. Install the dependencies(note, this is NOT npm install)
        $ npm run install-dependencies

4. Build the clients
        $ npm run build

5.  Run the app

        $ npm run start-dev
      The app should be visible on http://localhost:8080

      if developing in [c9.io](http://c9.io)

        $ npm run start-c9



## Testing

1. Run the tests

        $ npm test

  It might take a little while to install a few extra requirements the first
  time. The npm test command is configured with a path to the google-cloud-sdk in
  `package.json` under scripts. You might have to find the location of your own
  installation and and adjust accordingly

  Running a single group of tests can be done using something like

      $ npm test -- --test-pattern blog_test.py


## Deploy

    npm run deploy


## Development Notes
- Clients
  Both the admin client and the main page client were creacted using
  [create-react-app](https://github.com/facebookincubator/create-react-app)
  cd into client directory and you'll get all the tools you
  get with create-react-app

- NPM workflows
  I'm using the scripts portion of the package.json in this library to make my life easier.
  Anything I might have to type regularly or something that I want to turn into
  a single task(like building on deploy) goes there.

- Adding a new python package

        $ pip install  <package name> -t python_modules
    Make sure to add the new package information to `requirements.txt`!

- Adding a new node.js package

        $ npm install <package name> --save
  The clients have separate package.json files so make sure to cd into the appropriate
  directory before installing.

See the app folder for most of the code



 ### Resources
 - Unit testing with app engine https://cloud.google.com/appengine/docs/standard/python/tools/localunittesting
 - Idea for test setup
   ** Flask setup http://flask.pocoo.org/docs/0.12/tutorial/testing/
   ** http://stackoverflow.com/questions/1896918/running-unittest-with-typical-test-directory-structure !
 - [unittest](https://docs.python.org/2/library/unittest.html) Python's built in test framework
 - [pytest](http://doc.pytest.org/en/latest/)
 - [building a react router](http://jamesknelson.com/routing-with-raw-react/)
 - [just suck it up and use react-router](https://reacttraining.com/react-router/web/guides/quick-start)
 
 ### TODO
 - https with let's encrypt and instructions onto the readme
 - tests on react 
 - put admin client back in
 
