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
from flask import render_template
from flask import request
from models.entry import *


app = Flask(__name__)


allowed_args = {
  'offset':lambda x: False if re.match('^\d+$', x) == None else True,
}


@app.route('/')
def front():
    """Show the front page"""
    return render_template('layouts/front.html')

@app.route('/blog')
def blog(title="",entry="",error=""):
    """Show the blog"""
    offset = get_url_arg('offset')
    entries =get_entries(offset)

    next_offset = 10;
    if len(entries) < 10:
        next_offset = 0;
    elif offset != '':
        next_offset += int(offset)
    return render_template('blog.html',
        title=title,
        entry=entry,
        error=error,
        entries=entries,
        offset= str(next_offset)
     )






@app.errorhandler(500)
def server_error(e):
    logging.exception('An error occurred during a request.')
    return """
    An internal error occurred: <pre>{}</pre>
    See logs for full stacktrace.
    """.format(e), 500


#####
# HELPERS
####
def get_entries(offset):
    real_offset = int(offset) if offset != '' else 0;
    return  Entry.query().order(-Entry.created).fetch(10, offset=real_offset)

def get_url_arg(argname):
    test = allowed_args[argname];
    value = request.args.get('offset', '')
    assert value == '' or test(value)
    return value
