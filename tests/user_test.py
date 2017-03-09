
from app import main
import os
import unittest

class TestUser(unittest.TestCase):

    def setUp(self):
        main.app.testing = True
        self.app = main.app.test_client()

    def tearDown(self):
        pass


    def test_login(self):
        pass

    def test_delete_comment(self):
        pass





