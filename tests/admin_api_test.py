
from app import main
import os
import unittest

class TestAdminApi(unittest.TestCase):

    def setUp(self):
        main.app.testing = True
        self.app = main.app.test_client()

    def tearDown(self):
        pass


    def test_login(self):
        # Should redirect to the blog
        #'/user/login'
        pass

    def test_logout(self):
        # Should redirect to the blog

        pass

    def test_manage(self):
        # Should redirect to the blog
        #user/manage
        pass


    def test_api_delete_comment(self):
        pass


    def test_delete_comment(self):
        pass





