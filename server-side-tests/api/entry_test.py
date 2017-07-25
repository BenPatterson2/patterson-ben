
from app import main
from app.models.entry import *
import datetime
import unittest
import json
from google.appengine.ext import testbed
from google.appengine.ext import ndb

class TestEntry(unittest.TestCase):
    complete_data = {
        'title': 'this is a title',
        'entry': 'this is an entry'
    }
    incomplete_data = {}

    def setUp(self):
        main.app.testing = True
        self.app = main.app.test_client()
        #Stubing google app engine
        self.testbed = testbed.Testbed()
        self.testbed.activate()
        self.testbed.init_datastore_v3_stub()
        self.testbed.init_memcache_stub()
        self.testbed.init_user_stub()
        ndb.get_context().clear_cache()
        Entry.created._auto_now = False

    def tearDown(self):
        self.testbed.deactivate()

    def loginUser(self, email='user@example.com', id='123', is_admin=False):
        self.testbed.setup_env(
            user_email=email,
            user_id=id,
            user_is_admin='1' if is_admin else '0',
            overwrite=True)

    def logoutUser(self):
        self.testbed.setup_env(
            user_email='',
            user_id='',
            user_is_admin='0',
            overwrite=True)

    def test_get(self):
        #get an existing entry
        single_entry = Entry(
            title='Fake Single',
            entry='This is a single entry',
            created=datetime.datetime.now()
        )
        single_id = single_entry.put()

        r = self.app.get('api/entry/{}'.format(single_id.id()))
        assert r.status_code == 200
        entry = json.loads(r.data.decode('utf-8'))
        assert entry['title'] == 'Fake Single'

        #try to get an nonexistant entry
        r2 = self.app.get('api/entry/999'.format(single_id.id()))
        assert r2.status_code == 404
        err_data = json.loads(r2.data.decode('utf-8'))


    def test_authenticated_post(self):
        self.loginUser(is_admin=True)

        #incomplete data
        r = self.post_json(self.incomplete_data)
        entry = json.loads(r.data.decode('utf-8'))
        assert r.status_code == 400

        #complete data
        r2 = self.post_json(self.complete_data)
        entry2 = json.loads(r2.data.decode('utf-8'))
        assert r2.status_code == 200
        #Should be getting back and id from newly created post
        assert entry2['id']


    def test_unauthenticated_put(self):
        single_entry = Entry(
            title='Fake Single',
            entry='This is a single entry',
            created=datetime.datetime.now()
        )
        single_id = single_entry.put()
        r = self.api(
             request_method='put',
             url='api/entry/{}'.format(single_id.id()),
             data= {
                 'title': 'thiis is a new title',
                 'entry':'this is an updated entry'
              }
            )
        assert r.status_code == 401

    def test_authenticated_put(self):
        self.loginUser(is_admin=True)

        single_entry = Entry(
            title='Fake Single',
            entry='This is a single entry',
            created=datetime.datetime.now()
        )
        single_id = single_entry.put()
        r = self.api(
             request_method='put',
             url='api/entry/{}'.format(single_id.id()),
             data= {
                 'title': 'thiis is a new title',
                 'entry':'this is an updated entry'
              }
            )
        assert r.status_code == 200
        #Should be getting back and id from newly created post
        entry2 = Entry.get_by_id(single_id.id())
        assert entry2.entry == 'this is an updated entry'


    def test_unauthenticated_post(self):
        single_entry = Entry(
            title='Fake Single',
            entry='This is a single entry',
            created=datetime.datetime.now()
        )
        single_id = single_entry.put()
        r = self.api(
            request_method='delete',
            url='api/entry/{}'.format(single_id.id())
        )
        entry = json.loads(r.data.decode('utf-8'))
        assert r.status_code == 401


    def test_unauthenticated_delete(self):
        self.loginUser(is_admin=False)
        single_entry = Entry(
            title='Fake Single',
            entry='This is a single entry',
            created=datetime.datetime.now()
        )
        single_id = single_entry.put()

        r = self.api(
            request_method='delete',
            url='api/entry/{}'.format(single_id.id())
        )
        assert r.status_code == 401
        not_deleted = Entry.get_by_id(single_id.id())
        assert not_deleted


    def test_authenticated_delete(self):
        self.loginUser(is_admin=True)
        single_entry = Entry(
            title='Fake Single',
            entry='This is a single entry',
            created=datetime.datetime.now()
        )
        single_id = single_entry.put()


        r = self.api(
            request_method='delete',
            url='api/entry/{}'.format(single_id.id())
        )
        assert r.status_code == 200
        was_deleted = Entry.get_by_id(single_id.id()) == None
        assert was_deleted


    def post_json(self, data):
        return self.api(
          request_method='post',
          data=data
        )

    def api(self,
        request_method='post',
        url='api/entry',
        data={}):
        return getattr(self.app,request_method)(
           url,
           data= json.dumps(data),
           content_type='application/json'
        )


