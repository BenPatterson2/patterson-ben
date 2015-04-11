
from google.appengine.ext import ndb


class Portfolio(ndb.Model): #places new entries into the database
    link = ndb.StringProperty()
    description = ndb.TextProperty()
    image = ndb.BlobProperty()
    date = ndb.DateTimeProperty(auto_now_add=True)
		

