import sys

sys.path.insert(0,'../python_modules/markdown')
import markdown
from markupsafe import Markup, escape
from google.appengine.ext import ndb
import math;

class Entry(ndb.Model): #places new entries into the database

	title = ndb.StringProperty(required = True)
	entry = ndb.TextProperty(required = True)
	created = ndb.DateTimeProperty(auto_now_add = True)
	updated = ndb.DateTimeProperty(auto_now_add = True)
	entry_html = ndb.TextProperty()


	def permalink(self):
		 return "/blog/entries/" + str(self.key.id())

	def markdown_content(self):
		return Markup( self.entry_html )

	def set_entry_html(self):
		self.entry_html =  markdown.markdown(self.entry)

	def to_json(self):
		return {
		  'entry':self.entry,
		  'title':self.title,
		  'created':self.created.strftime("%B %d, %Y - %H:%M"),
		   'id': self.key.id()
		}



