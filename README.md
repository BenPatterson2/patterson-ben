
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

4. Build the client
        $ npm run build

5.  Run the app locally

        $ npm run start-dev
    This starts the  app including the google app engine extras at
    http://localhost:8080

      if developing in [c9.io](http://c9.io)

        $ npm run start-c9

## API

- `api/entries?offset=int`

   returns entries in groups of ten depending on the offset

- `api/entry/:entry_id` GET

  returns
      {
        title:'title'
        entry: 'entry'
      }

- `api/entry/` POST

  ( login required )
    Creates a new entry
    login required

    Request data =
      {
        title: *required*,
        entry:*required*
      }

- `api/entry/:entry_id` PUT

  ( login required )
  edits an entry
  
    Request data =
      {
          title: *required*,
          entry:*required*
      }

- `api/entry/:entry_id` DELETE

  ( login required )
   deletes an entry

## Testing

1. Running the tests

        $ npm test


  The npm test command is configured with a path to the google-cloud-sdk in
  `package.json` under scripts.
  You may have to find the location of your own installation of the google-cloud-sdk and and adjust the package.json file accordingly

  Running a single group of tests can be done using

      $ npm test -- --test-pattern blog_test.py


## Deploying

    npm run deploy


## Development Notes
- Client
  The client was created using
  [create-react-app](https://github.com/facebookincubator/create-react-app)
  cd into client directory and you'll get all the tools you
  get with  
[create-react-app](https://github.com/facebookincubator/create-react-app)

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

### SSL setup

 - Using [let's encrypt](https://letsencrypt.org/) with google app engine requires updating
 the cert every three months

 - [let's encrypt and GAE](https://www.jeffgodwyll.com/posts/2016/letsencrypt/)

    Key difference is using certbot as a command line. See next line


- [installing certbot ubuntu](https://certbot.eff.org/#ubuntuxenial-other)

### Resources
 - Unit testing with app engine https://cloud.google.com/appengine/docs/standard/python/tools/localunittesting
 - Idea for test setup
   ** Flask setup http://flask.pocoo.org/docs/0.12/tutorial/testing/
   ** http://stackoverflow.com/questions/1896918/running-unittest-with-typical-test-directory-structure !
 - [unittest](https://docs.python.org/2/library/unittest.html) Python's built in test framework
 - [pytest](http://doc.pytest.org/en/latest/)
 - [building a react router](http://jamesknelson.com/routing-with-raw-react/)
 - [react-router quick-start](https://reacttraining.com/react-router/web/guides/quick-start)

 ### TODO
 - fix pagination/replace with something prebuilt
 - tests on react
 - put admin client back in

