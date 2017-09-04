

from flask import request
import json
from app.models.entry import Entry
from app.models.user import User
from flask_restful import Resource
from marshmallow import Schema, fields, ValidationError
from werkzeug.exceptions import BadRequest, NotFound

class Validator(Schema):
    title = fields.Str(required=True)
    entry = fields.Str(required=True)
    published = fields.Boolean(required=True)


# Decoratores

def authenticate(func):
    def wrapper(s, **kwargs):
        acct = User.authenticate()
        if acct:
            return func(s,acct=acct, **kwargs)
    return wrapper

def validate_json(func):
    def wrapper(s,**kwargs):
        json_data = request.get_json()
        if not json_data:
            raise BadRequest('Empty request')
        try:
            params = Validator(strict=True).load(json_data)
        except ValidationError as err:
            raise BadRequest(err.messages)
        return func(s, json_data=json_data, **kwargs)
    return wrapper

def get_entry(func):
    def wrapper(s, entry_id,**kwargs):
        entry = Entry.get_by_id(entry_id)
        if entry:
            return func(s, entry, **kwargs)
        else:
             raise NotFound('not found')
    return wrapper




class EntryApi(Resource):

    @get_entry
    def get(self, entry):
        return entry.to_json()

    @authenticate
    @validate_json
    @get_entry
    def put(self,entry, json_data=None, **kwargs):
        entry.title = json_data['title']
        entry.entry = json_data['entry']
        entry.published = json_data['published']
        entry.put()
        return entry.to_json()

    @authenticate
    @get_entry
    def delete(self, entry, **kwargs):
        entry.key.delete()
        #REVIEW make sure that the cache is fixed when this is put back in
        return { 'message': 'Entry {} has been deleted'.format(entry.key.id())  }

class CreateEntryApi(Resource):

    @authenticate
    @validate_json
    def post(self,json_data=None, **kwargs):
        entry = Entry(**json_data)
        entry.put()
        return entry.to_json()




