
from app import main
from app.models.entry import *
import datetime
import unittest
import json
from google.appengine.ext import testbed
from google.appengine.ext import ndb

class TestStatic(unittest.TestCase):

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

    def tearDown(self):
        self.testbed.deactivate()


    def test_login(self):
        r = self.app.get('/micro-manager/login')
        page =  r.data.decode('utf-8')
        assert r.status_code == 302

    def test_logout(self):
        r = self.app.get('/micro-manager/logout')
        page =  r.data.decode('utf-8')
        assert r.status_code == 302


   #  This is for testing a post
   # return self.app.post('/login', data=dict(
   #      username=username,
   #      password=password
   #  ), follow_redirects=True)