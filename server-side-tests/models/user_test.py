
from app import main
from app.models.user import User
import datetime
import unittest
import json
from werkzeug.exceptions import Unauthorized
from google.appengine.ext import testbed
from google.appengine.ext import ndb

class TestUser(unittest.TestCase):
    def setUp(self):

        #Stubing google app engine
        self.testbed = testbed.Testbed()
        self.testbed.activate()
        self.testbed.init_datastore_v3_stub()
        self.testbed.init_memcache_stub()
        self.testbed.init_user_stub()
        ndb.get_context().clear_cache()

    def tearDown(self):
        self.testbed.deactivate()

    def test_user(self):
        try:
            User.authenticate()
            assert False
        except Unauthorized:
            assert True
            return
        assert False

