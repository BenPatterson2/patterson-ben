
from app import main
from app.models.entry import *
import datetime
import unittest
import json
from google.appengine.ext import testbed
from google.appengine.ext import ndb

class TestEntries(unittest.TestCase):
    entry_count = 30
    def setUp(self):
        main.app.testing = True
        self.app = main.app.test_client()
        #Stubbing google app engine
        self.testbed = testbed.Testbed()
        self.testbed.activate()
        self.testbed.init_datastore_v3_stub()
        self.testbed.init_memcache_stub()
        self.testbed.init_user_stub()
        ndb.get_context().clear_cache()
        Entry.created._auto_now = False

        entries = [
          Entry(
            title='Fake ' + str(self.entry_count - x),
            entry='This entry' + str(self.entry_count- x),
            created=datetime.datetime.now() - datetime.timedelta(hours=x),
            published=True
           ) for x in range(self.entry_count)
        ]
        ndb.put_multi(entries)

    def tearDown(self):
        self.testbed.deactivate()


    def test_entries(self):
        r = self.app.get('api/entries')
        page =  r.data.decode('utf-8')
        entries =  json.loads(page)
        assert len(entries['posts']) == 10
        assert entries['total'] == self.entry_count
        assert entries['posts'][0]['title'] == 'Fake 30'
        assert isinstance(entries['posts'][0]['timestamp'], int)

    def test_entries_offset(self):
        offset = 20
        r = self.app.get('api/entries?offset={0}'.format(offset))
        assert r.status_code == 200
        page =  r.data.decode('utf-8')
        titles = ['Fake 10', 'Fake 9']
        for title in titles:
            assert title in page

    def test_entries_headers(self):
        r = self.app.get('api/entries')
        assert r.status_code == 200
        assert r.headers['Content-Range'] == '0-10/30'


