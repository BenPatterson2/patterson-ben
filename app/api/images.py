from flask_restful import reqparse
from app.models.uploaded_image import *
from app.models.user import User
from flask_restful import Resource
from flask import Response
import json

parser = reqparse.RequestParser()
parser.add_argument('offset', type=int )

class ImagesApi(Resource):
    def get(self):
        args = parser.parse_args()
        offset = args['offset'] or 0
        images = UploadedImage.query().order(-UploadedImage.created).fetch(10, offset=offset)
        total = UploadedImage.query().count()
        res_json = { 'images': [ image.to_json() for image in images ], 'total':total }
        resp = Response(json.dumps(res_json))
        resp.headers.extend({
            'Content-Range': '{}-{}/{}'.format(offset, offset + 10, total ),
            'Content-Type':'application/json'
            })
        return resp

