from flask_restful import reqparse
from app.models.entry import *
from app.models.user import User
from flask_restful import Resource
from flask import Response
import json

parser = reqparse.RequestParser()
parser.add_argument('offset', type=int )

class EntriesApi(Resource):
    def get(self):
        args = parser.parse_args()
        offset = args['offset'] or 0
        if User.is_admin():
            entries = get_entries(offset, True)
            total = Entry.query().count()
        else:
            entries = get_entries(offset, False)
            total = Entry.query(Entry.published == True).count()
        res_json = { 'posts': [entry.to_json() for entry in entries ], 'total':total }
        resp = Response(json.dumps(res_json))
        resp.headers.extend({
            'Content-Range': '{}-{}/{}'.format(offset, offset + 10, total ),
            'Content-Type':'application/json'
            })
        return resp



def get_entries(offset, admin):
    if admin:
        return  Entry.query().order(-Entry.created).fetch(10, offset=offset)
    return Entry.query(Entry.published == True).order(-Entry.created).fetch(10, offset=offset)
