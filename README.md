
# Benpatterson.io

## Requirements

- Google App Engine for Python
  - Ubuntu:  [https://cloud.google.com/sdk/docs/#deb](https://cloud.google.com/sdk/docs/#deb)
  - Mac: [https://cloud.google.com/sdk/docs/#mac](https://cloud.google.com/sdk/docs/#mac)
- [pip](http://pip.readthedocs.io/en/stable/)
- [Node.js](https://nodejs.org/en/)

## Run Locally

1. Clone the repo

        $ git clone git@github.com:BenRuns/patterson-ben.git


3. Install the dependencies

        $ npm run install-dependencies

4.  Run the app

        $ npm run start-dev
      The app should be visble on http://localhost:8080

      if developing in [c9.io](http://c9.io)

        $ dev_appserver.py --host=$IP --port=$PORT app.yaml

## Testing

1. Run the tests

        $ npm test
  It might take a little while to install a few extra requirements the first
  time. The npm test command is configured with a path to the google-cloud-sdk in
  `package.json` under scripts. You might have to find the location of your own
  installation and and adjust accordingly

## Deploy

    gcloud app deploy


## Development Notes

- Adding a new python package

        $ pip install  <package name> -t lib
    Make sure to add the new package information to `requirements.txt`!

- Adding a new node.js package

        $ npm install <package name> --save

See the app folder for most of the code



 ### Resources
 - Unit testing with app engine https://cloud.google.com/appengine/docs/standard/python/tools/localunittesting
 - Idea for test setup
   ** Flask setup http://flask.pocoo.org/docs/0.12/tutorial/testing/
   ** http://stackoverflow.com/questions/1896918/running-unittest-with-typical-test-directory-structure !
 - [unittest](https://docs.python.org/2/library/unittest.html) Python's built in test framework
 - [pytest](http://doc.pytest.org/en/latest/)
