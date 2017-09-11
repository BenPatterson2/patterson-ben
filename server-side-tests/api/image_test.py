import os
from app import main
from app.models.uploaded_image import *
import datetime
import unittest
import json
from google.appengine.api import images
from google.appengine.ext import testbed
from google.appengine.ext import ndb
import uuid
import base64
import md5


cwd = os.getcwd()

class TestImage(unittest.TestCase):
    def setUp(self):
        main.app.testing = True
        self.app = main.app.test_client()
        #Stubing google app engine
        self.testbed = testbed.Testbed()
        self.testbed.activate()
        self.testbed.init_all_stubs()

        ndb.get_context().clear_cache()
        UploadedImage.created._auto_now = False

    def tearDown(self):
        self.logoutUser()
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
    # NOTE - Testing is pain because it the blobstore stub isn' that great
    # Posting an item to the blobstore seems to require posting to a generated
    # url like ` blobstore.generate_uri('/upload')`

    # def test_get(self):
    #     pass
    #     # with open(cwd + '/server-side-tests/api/foo.jpg') as img:
    #     #     upload = images.Image(img).resize(width=200)
    #     #     single_image = UploadedImage(img=upload,created=datetime.datetime.now())
    #     #     single_image.put()
    #     #     r = self.app.get('api/image/{}'.format(single_image.key.id()))
    #     #     assert r.status_code == 200

    def test_get_uri(self):
        self.loginUser(is_admin=True)
        r = self.app.get('api/image')
        page =  r.data.decode('utf-8')
        data =  json.loads(page)
        #TODO test URI
        assert r.status_code == 200


    # def test_authenticated_post(self):
    #     pass
    #     # self.loginUser(is_admin=True)
    #     # with open(cwd + '/server-side-tests/api/foo.jpg') as img:
    #     #     r = self.post_image(data=dict(image=img))
    #     #     assert r.status_code == 200

    # def test_unauthenticated_put(self):
    #     pass
    #
    # def test_authenticated_put(self):
    #     pass
    #
    #
    # def test_unauthenticated_post(self):
    #     pass
    #
    #
    # def test_unauthenticated_delete(self):
    #     pass
    #
    #
    # def test_authenticated_delete(self):
    #     pass
    #
    #
    # def post_image(self,
    #     request_method='post',
    #     url='api/image',
    #     data={}):
    #     data = json.dumps({})
    #     message =( "Content-Type: application/octet-stream\r\nContent-Length: " +
    #     str(len(data)) + "\r\nContent-MD5: " +
    #     base64.b64encode(md5.new(data).hexdigest()) +
    #     "\r\nX-AppEngine-Cloud-Storage-Object: /gs" +
    #     ""+
    #     "\r\ncontent-disposition: form-data; name=\"" + 'image' +
    #     "\"; filename=\"" + 'foo.jpg' +
    #     "\"\r\nX-AppEngine-Upload-Creation: 2015-07-17 16:19:55.531719\r\n\r\n")
    #
    #
    #     return getattr(self.app,request_method)(
    #        url,
    #        data = dict(image=[
    #        ('foo.jpg', message,
    #        "message/external-body; blob-key=\"encoded_gs_file:blablabla\"; access-type=\"X-AppEngine-BlobKey\"")]),
    #        content_type='multipart/form-data'
    #     )

# from google.appengine.api import datastore
# import uuid
# import base64
# import md5
#
# def testSomething(self):
#   upload_url = self.testapp.post('/path/to/create_upload_url/handler').body
#   response = self.upload_blobstore_file(upload_url, "file", "myfile.txt", "MYDATA1").json
#   # Test something on the response from the success handler and/or backing storage
#
# def upload_blobstore_file(self, upload_url, field, filename,
#     contents, type = "application/octet-stream"):
#   session = datastore.Get(upload_url.split('/')[-1])
#   new_object = "/" + session["gs_bucket_name"] + "/" + str(uuid.uuid4())
#   self.storage_stub.store(new_object, type, contents)
#
#   message = "Content-Type: application/octet-stream\r\nContent-Length: " + str(len(contents)) + "\r\nContent-MD5: " + base64.b64encode(md5.new(contents).hexdigest()) + "\r\nX-AppEngine-Cloud-Storage-Object: /gs" + new_object.encode("ascii") + "\r\ncontent-disposition: form-data; name=\"" + field + "\"; filename=\"" + filename + "\"\r\nX-AppEngine-Upload-Creation: 2015-07-17 16:19:55.531719\r\n\r\n"
#   return self.testapp.post(session["success_path"], upload_files = [
#   (field, filename, message, "message/external-body; blob-key=\"encoded_gs_file:blablabla\"; access-type=\"X-AppEngine-BlobKey\"")
# ])

