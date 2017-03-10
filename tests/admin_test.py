
from app import main
import os
import unittest

class TestAdminView(unittest.TestCase):

    def setUp(self):
        main.app.testing = True
        self.app = main.app.test_client()

    def tearDown(self):
        pass

#Test can access the api page 
