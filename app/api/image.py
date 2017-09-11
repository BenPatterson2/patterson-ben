from flask import request, make_response
from flask import Response
import json
import os
from app.models.uploaded_image import UploadedImage
from app.models.user import User
from flask_restful import Resource,reqparse, abort
from google.appengine.ext import blobstore
from google.appengine.api import app_identity

from werkzeug.exceptions import BadRequest, NotFound
from werkzeug.datastructures import FileStorage
from werkzeug.http import parse_options_header


#BUCKET_NAME = os.environ.get('BUCKET_NAME',
                              # app_identity.get_default_gcs_bucket_name())

# Decorators



class FileStorageArgument(reqparse.Argument):
    """This argument class for flask-restful will be used in
    all cases where file uploads need to be handled."""
    # Taken from https://gist.github.com/RishabhVerma/7228939
    def convert(self, value, op):
        if self.type is FileStorage:  # only in the case of files
            # this is done as self.type(value) makess the name attribute of the
            # FileStorage object same as argument name and value is a FileStorage
            # object itself anyways
            return value

        # called so that this argument class will also be useful in
        # cases when argument type is not a file.
        super(FileStorageArgument, self).convert(*args, **kwargs)

def authenticate(func):
    def wrapper(s, **kwargs):
        acct = User.authenticate()
        if acct:
            return func(s,acct=acct, **kwargs)
    return wrapper


def get_image(func):
    def wrapper(s, image_id,**kwargs):
        image = UploadedImage.get_by_id(image_id)
        if image:
            return func(s, image, **kwargs)
        else:
             raise NotFound('not found')
    return wrapper

class ImageApi(Resource):

    @get_image
    def get(self,image):
        return image.to_json()

    @authenticate
    @get_image
    def put(self,entry, json_data=None, **kwargs):
        pass

    @authenticate
    @get_image
    def delete(self, image, **kwargs):
        image.key.delete()
        #REVIEW make sure that the cache is fixed when this is put back in
        return { 'message': 'Entry {} has been deleted'.format(entry.key.id())  }

class CreateImageApi(Resource):
    parser = reqparse.RequestParser(argument_class=FileStorageArgument)
    parser.add_argument('image',
       required=True,
       type=FileStorage,
       location='files')

    @authenticate
    def get(self, acct):
        bucket_name = os.environ.get('BUCKET_NAME',
                                     app_identity.get_default_gcs_bucket_name())
        uploadUri = blobstore.create_upload_url('/api/image', gs_bucket_name=bucket_name)
        return { 'uri': uploadUri }

    @authenticate
    def post(self, acct):
        #TODO graceful failure
        args = self.parser.parse_args()
        image = args['image']
        headers =  parse_options_header(image.headers['Content-Type'])
        img = UploadedImage(img=headers[1]['blob-key'])
        img.put()
        return img.to_json()




