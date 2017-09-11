
from app import main
from app.models.uploaded_image import *
import datetime
import unittest
import json
from google.appengine.ext import testbed
from google.appengine.ext import ndb

class TestImage(unittest.TestCase):
    image_count = 30
    images = []
    def setUp(self):
        main.app.testing = True
        self.app = main.app.test_client()
        #Stubbing google app engine
        self.testbed = testbed.Testbed()
        self.testbed.activate()
        self.testbed.init_all_stubs()

        ndb.get_context().clear_cache()
        UploadedImage.created._auto_now = False

        self.images = [
          UploadedImage(
            created=datetime.datetime.now() - datetime.timedelta(hours=x),
            img='blob_key'

           ) for x in range(self.image_count)
        ]
        ndb.put_multi(self.images)

    def tearDown(self):
        self.testbed.deactivate()


    def test_images(self):
        r = self.app.get('api/images')
        page =  r.data.decode('utf-8')
        images =  json.loads(page)
        assert len(images['images']) == 10
        assert images['total'] == self.image_count


    def test_images_offset(self):
        offset = 20
        r = self.app.get('api/images?offset={0}'.format(offset))
        assert r.status_code == 200
        page =  r.data.decode('utf-8')
        for image in self.images[20:]:
            assert str(image.key.id()) in page

    def test_images_headers(self):
        r = self.app.get('api/images')
        assert r.status_code == 200
        assert r.headers['Content-Range'] == '0-10/30'


