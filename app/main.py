# Copyright 2015 Google Inc. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

# [START app]
import logging
import os
import re

from flask import Flask
from flask import render_template, redirect, send_from_directory
from flask_restful import reqparse
from models.user import User

from api.entry import CreateEntryApi, EntryApi
from api.entries import EntriesApi


from flask_restful import Resource, Api
from flask_cors import CORS, cross_origin
app = Flask(__name__)
cors = CORS(app, resources={r"/api/*": {"origins": "*"}})

api = Api(app)

api.add_resource(EntryApi, '/api/entry/<int:entry_id>')
api.add_resource(CreateEntryApi, '/api/entry')
api.add_resource(EntriesApi, '/api/entries')


@app.route("/micro-manager/login")
def login():
    return redirect(User.create_login_url('micro-manager'))

@app.route("/micro-manager/logout")
def logout():
    return redirect(User.create_logout_url('/'))


@app.errorhandler(500)
def server_error(e):
    logging.exception('An error occurred during a request.')
    return """
    An internal error occurred: <pre>{}</pre>
    See logs for full stacktrace.
    """.format(e), 500
