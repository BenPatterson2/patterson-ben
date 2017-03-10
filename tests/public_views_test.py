
from app import main
from app.models.entry import *
import datetime
import unittest
from google.appengine.ext import testbed
from google.appengine.ext import ndb

class TestPublicViews(unittest.TestCase):
    entry_count = 30
    def setUp(self):
        main.app.testing = True
        self.app = main.app.test_client()
        #Stubing google app engine
        self.testbed = testbed.Testbed()
        self.testbed.activate()
        self.testbed.init_datastore_v3_stub()
        self.testbed.init_memcache_stub()
        ndb.get_context().clear_cache()
        Entry.created._auto_now = False


        entries = [
          Entry(
            title='Fake ' + str(self.entry_count - x),
            entry='This entry' + str(self.entry_count- x),
            created=datetime.datetime.now() - datetime.timedelta(hours=x)
           ) for x in range(self.entry_count)
        ]
        ndb.put_multi(entries)

    def tearDown(self):
        self.testbed.deactivate()

    def test_index(self):
        r = self.app.get('/')
        assert r.status_code == 200
        assert 'Ben Patterson' in r.data.decode('utf-8')

    def test_blog(self):
        titles = ['Fake 30', 'Fake 28']
        r = self.app.get('/blog')
        assert r.status_code == 200
        page =  r.data.decode('utf-8')
        assert 'Ben\'s Blog' in page
        for title in titles:
            assert title in page

    def test_blog_offset(self):
        offset = 20
        r = self.app.get('/blog?offset={0}'.format(offset))
        assert r.status_code == 200
        page =  r.data.decode('utf-8')
        titles = ['Fake 10', 'Fake 9']
        for title in titles:
            assert title in page

    def test_api(self):
        pass