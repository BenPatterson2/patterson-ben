
from app import main
import os
import unittest

class HelloWorldCase(unittest.TestCase):

    def setUp(self):
        main.app.testing = True
        self.app = main.app.test_client()

    def tearDown(self):
        pass
        
    def test_index(self):
        r = self.app.get('/')
        assert r.status_code == 200
        assert 'Ben Patterson' in r.data.decode('utf-8')


