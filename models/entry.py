
from google.appengine.ext import db


class Entry(db.Model): #places new entries into the database

    title = db.StringProperty(required = True)
    entry = db.TextProperty(required = True)
    created = db.DateTimeProperty(auto_now_add = True)