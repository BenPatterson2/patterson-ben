import sys

sys.path.insert(0,'../python_modules/markdown')
import markdown
from google.appengine.ext import ndb
import math;
import datetime

epoch = datetime.datetime.utcfromtimestamp(0)
class Entry(ndb.Model): #places new entries into the database

	title = ndb.StringProperty(required = True)
	entry = ndb.TextProperty(required = True)
	created = ndb.DateTimeProperty(auto_now_add = True)
	published = ndb.BooleanProperty(default = False)
	updated = ndb.DateTimeProperty(auto_now_add = True)
	entry_html = ndb.TextProperty()

	def to_json(self):
		return {
		  'entry':self.entry,
		  'title':self.title,
		  'created':self.created.strftime("%B %d, %Y - %H:%M"),
		  'timestamp': int((self.created - epoch).total_seconds() * 1000.0),
		   'id': self.key.id(),
		   'published': self.published
		}



