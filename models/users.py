from google.appengine.ext import db

class User(db.Model): #places new entries into the database

    username= db.StringProperty(required = True)
    password = db.TextProperty(required = True)
    email = db.EmailProperty()