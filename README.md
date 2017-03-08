
# Benpatterson.io

## Requirements

- [Google App Engine for Python](https://cloud.google.com/appengine/docs/flexible/python/quickstart)
- [pip](http://pip.readthedocs.io/en/stable/)
- [Node](https://nodejs.org/en/)

## Run Locally

1. Clone the repo
    
        $ git clone git@github.com:BenRuns/patterson-ben.git
 
2. Set up a python virual env
  
    If you don't have [virtualenv](https://virtualenv.pypa.io/en/stable/) installed  `$ sudo pip install virtualenv`
    
        $ cd patterson-ben
        $ virtualenv env
    
    To activate the environment
    
        $ . env/bin/activate
    
    To deactivate the env
    
        $ deactivate

3. Install the dependencies
    
        $ npm run install-dependencies

4.  Run the app
    
        $ dev_appserver.py --port=9999 app.yaml
      
      if developing in [c9.io](http://c9.io)
      
        $ dev_appserver.py --host=$IP --port=$PORT app.yaml`
## Testing

1. Install [pytest](http://doc.pytest.org/en/latest/)
    
        $ pip install pytest`
2. Run the tests
    
        
## Deploy

    gcloud app deploy


## Development 

- Adding a new python package
    
        $ pip install  <package name> -t lib `
    make sure to add the new package information to `requirements.txt`. 

- Adding a new node.js package
    
        $ npm install <package name> --save`




 ### Resources
 - Idea for test setup
   ** Flask setup http://flask.pocoo.org/docs/0.12/tutorial/testing/
   ** http://stackoverflow.com/questions/1896918/running-unittest-with-typical-test-directory-structure !
 - [unittest](https://docs.python.org/2/library/unittest.html) Python's built in test framework
 - [pytest](http://doc.pytest.org/en/latest/)
