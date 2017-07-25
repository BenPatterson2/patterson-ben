from google.appengine.api import users
from google.appengine.ext import ndb
from werkzeug.exceptions import Unauthorized

class User(ndb.Model): #places new entries into the database
    @staticmethod
    def authenticate():
      user = users.get_current_user()
      if not user or not users.is_current_user_admin():
          raise Unauthorized
      return user

    @staticmethod
    def create_login_url(redirect_to):
        return users.create_login_url(redirect_to)
        
    @staticmethod
    def create_logout_url(redirect_to):
        return users.create_logout_url(redirect_to)
