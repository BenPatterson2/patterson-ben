from google.appengine.ext import ndb
from google.appengine.api import images
import datetime
epoch = datetime.datetime.utcfromtimestamp(0)
class UploadedImage(ndb.Model):
	created = ndb.DateTimeProperty(auto_now_add = True)
	img = ndb.StringProperty(required=True)
	updated = ndb.DateTimeProperty(auto_now_add = True)

	def serving_uri(self):
		return images.get_serving_url(self.img, secure_url=True)

	def to_json(self):
		return {
		  'servingUri':self.serving_uri(),
		  'timestamp': int((self.created - epoch).total_seconds() * 1000.0),
		  'updated': int((self.updated - epoch).total_seconds() * 1000.0),
		  'id': self.key.id()
		}
