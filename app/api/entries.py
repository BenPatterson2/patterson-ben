

from flask_restful import reqparse
from app.models.entry import *
from flask_restful import Resource

parser = reqparse.RequestParser()
parser.add_argument('offset', type=int )

class EntriesApi(Resource):
    def get(self):
        args = parser.parse_args()
        entries = get_entries(args['offset'])
        return { 'entries': [entry.to_json() for entry in entries ] }





def get_entries(offset):
    real_offset = offset if offset else 0;
    return  Entry.query().order(-Entry.created).fetch(10, offset=real_offset)
