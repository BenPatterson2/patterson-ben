#!/usr/bin/env python
#
# Copyright 2007 Google Inc.
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

#


import os
import re
from string import letters
import utils.CBM
import hashlib
import hmac
import random
from private import secret
import string

import webapp2
import jinja2
import json
import urllib2
import logging
import datetime 

from google.appengine.api import memcache
from google.appengine.ext import db


template_dir =([os.path.join(os.path.dirname(__file__),"views/navigation"),
         os.path.join(os.path.dirname(__file__),"views/layouts"),
         os.path.join(os.path.dirname(__file__),"views")])

jinja_env = jinja2.Environment(loader = jinja2.FileSystemLoader(template_dir),
                               
                               autoescape = True)
def render_str(template, **params):
    t = jinja_env.get_template(template)
    return t.render(params)

def make_secure_val(val):
    return '%s|%s' % (val, hmac.new(secret, val).hexdigest())

def check_secure_val(secure_val):
    val = secure_val.split('|')[0]
    if secure_val == make_secure_val(val):

        return val

def make_salt():
    return ''.join(random.choice(string.letters) for x in xrange(5))

#

def make_pw_hash(name, pw, salt=None):
    if not salt:
        salt = make_salt()
    h = hashlib.sha256(name + pw + salt).hexdigest()
    return '%s,%s' % (h, salt)

def valid_pw(name, pw, h):
    ###Your code here
    salt = h.split(',')[1]
  
    
    check = make_pw_hash(name,pw,salt)
    if h == check:
        return True
    else:
        return None



class BaseHandler(webapp2.RequestHandler):
    def render(self, template, **kw):



        self.response.out.write(render_str(template, **kw))

    def write(self, *a, **kw):
        self.response.out.write(*a, **kw)
############################################
## MAIN PAGE
############################################


class MainHandler(webapp2.RequestHandler):
    def get(self):
        self.response.write('come back later please')
        self.response.write(str(datetime.datetime.now()))



#####################################
# FREIGHT CALCULATOR
#####################################

class BoxSet(object):

    def __init__(self, pcs=1,dims=[0,0,0],weight=0, metric="0", measure="0"):
        """
        sets as original entered 
        weight is stored per pc

        """
        self.weight_type = "LBS" if metric == "0" else "KGS"
        self.measure_type = "IN" if measure == "0" else "CM"

        self.pcs = max(pcs,1) 
        self.dims = dims
        self.weight_pc = weight/self.pcs


    def weight(self):
        """
        returns total weight as per the set's weight type designation
        """
        return self.weight_pc * self.pcs 


    def kgs(self):
        """
        returns total weight per set in kgs
        """
        return self.weight()/2.2046 if self.weight_type == "LBS" else self.weight()

    def cft(self):# calculate cubic feet using inches as inputs
        """
        returns total cft
        """
        return self.pcs * reduce(lambda x, y: x*y, self.dims_in())/1728

    def lbs(self):
        """
        returns total weight per set in lbs
        """
        return self.weight() * 2.2046 if self.weight_type == "KGS" else self.weight()

    def dims_in(self):
        """
        returns total an array of [length,width,height] listed as inches
        """
        convertin = lambda x: x/2.54 if self.measure_type == "CM" else  x
        return [ convertin(item) for item in self.dims ]

    def dims_cm(self):

        """
        returns total an array of [length,width,height] listed in inches

        """
        convertcm = lambda x: x * 2.54 if self.measure_type == "IN" else  x
        return [ convertcm(item) for item in self.dims ]

    def chargeable(self):
        """
        calculates dimensional weight for air travel
        """

        return max((self.pcs * reduce(lambda x, y: x*y, self.dims_in() ) )/366, self.kgs() )

    def m3(self):
        """
         calculates cubic meters using cm as inputs
        """
        return (self.pcs * reduce(lambda x, y: x*y, self.dims_cm() ) )/1000000.0

        



class Clear(BaseHandler):

    def get(self):
        self.response.headers.add_header('Set-Cookie', 'lines=1; Path=/')
        self.redirect("/container")


class LoadPlan(BaseHandler):

    def get(self):
        self.render("layouts/container.html",boxes = BoxSet())
    


    def Clear(self):
        self.response.headers.add_header('Set-Cookie', 'lines=1; Path=/')
        self.redirect("/container")


    def post(self): 

        """
        Formats the input from the form to enter into 
        BoxSet instance. It chooses the higher of pcs * per pc weight
        or total weight listed on form
        sets negative inputs to abs value

        """

        format = lambda x: 0 if not self.request.get(x) else abs(float(self.request.get(x)))

        pcs = max(int(self.request.get("pcs")),1) 
        dims = [ format(dim) for dim in ["length","width","height"]]
       
        metric = self.request.get("metric")  if self.request.get("metric")  else "0"
        measure = self.request.get("measure") if self.request.get("measure")  else "0"

        total_weight = format("weight")
        pc_weight = format("weight_pc")
        weight = max((pc_weight * pcs) , total_weight)

        boxes = BoxSet(pcs,dims,weight,metric,measure)
       
        self.render("layouts/container.html",boxes = boxes )

#####################################
# BLOG STUFF
#####################################




class NewPost(BaseHandler): #renders the page to post items too. The front handler(Blog) inherits from this class
    def render_front(self,title="",entry="",error=""):
        self.render("newpost.html", title=title, entry=entry, error=error,)
    def get(self):
        self.render_front()

    def post(self):
        title = self.request.get("subject")
        entry = self.request.get("content")

        if title and entry:
            e = Entry(title = title, entry = entry)
            
            e.put()
            link = e.key().id()
            memcache.delete("top")


            self.response.out.write(link)


            memcache.set(str(link),([e],datetime.datetime.now()))

            self.redirect("/blog/entries/"+str(link))

        else:
            error =" we need both a title and an entry"
            self.render_front(title, entry, error)


def top_pages():
    key = 'top'
    memcache.set('time', datetime.datetime.now())

    logging.info("DB_QUERY")
    entries = db.GqlQuery("SELECT * FROM Entry ORDER BY created  DESC LIMIT 10")
    #entries = list(entries)


    memcache.set(key,entries)
    return entries

class Blog(NewPost):#renders the front page and imports from new post



    def render_front(self,title="",entry="",error=""):
        if memcache.get("top") is not None:
            entries = memcache.get("top")
            now = datetime.datetime.now()
            then = memcache.get('time')
            seconds = str((now-then).seconds)
        else:
        
            entries = top_pages()
            seconds = "0"
           

        self.render("blog.html", title=title, entry=entry, error=error, entries=entries, cached=seconds,)

class Entry(db.Model): #places new entries into the database

    title = db.StringProperty(required = True)
    entry = db.TextProperty(required = True)
    created = db.DateTimeProperty(auto_now_add = True)

class User(db.Model): #places new entries into the database

    username= db.StringProperty(required = True)
    password = db.TextProperty(required = True)
    
    email = db.EmailProperty()




class Entries(BaseHandler): #for the permalinking

    def render_front(self,product_id):
        ID=int(product_id)
        test = memcache.get(str(ID))
        if test == None:

            entries = db.GqlQuery("SELECT * FROM Entry where name = %s" %ID)
            entries = list(entries)
            now = datetime.datetime.now()
            memcache.set(str(ID), (entries, now))
            
            seconds = "0"
        else:
            entries = memcache.get(str(ID))[0]
            now = datetime.datetime.now()
            then = memcache.get(str(ID))[-1]
            seconds = str((now-then).seconds)

        self.render("blog.html", entries =entries, cached = seconds)

    def get(self,product_id):
        self.render_front(product_id)

class SignUp(BaseHandler):
    def get(self):
        #self.response.headers['Content-Type'] ='text/plain'
        self.render("signup.html",username="",username_error="",password="",password_error="",
                   verify="",verify_error="",email="",email_error="")

        

    USER_RE = re.compile(r"^[a-zA-Z0-9_-]{3,20}$" )
    PASSWORD_RE = re.compile(r"^.{3,20}$")
    EMAIL_RE = re.compile(r"^[\S]+@[\S]+\.[\S]+$")

    def valid_username(self,username):

        return self.USER_RE.match(username)

    def available_username(self,username):
        if User.get_by_key_name (username, parent=None) != None:
            return False
        else:
            return True

    def valid_password(self, password):
        return self.PASSWORD_RE.match(password)

    def text_match(self,text1,text2):
        return text1 == text2

    def valid_email(self,email):
        return self.EMAIL_RE.match(email)

    def set_secure_cookie(self, name, val):
        cookie_val = make_secure_val(val)
        self.response.headers.add_header(
            'Set-Cookie',
            '%s=%s; Path=/' % (name, cookie_val))

    def read_secure_cookie(self, name):
        cookie_val = self.request.cookies.get(name)
        return cookie_val and check_secure_val(cookie_val)

    def post(self):
        user_username = self.request.get('username')

        user_password = self.request.get('password')

        user_verify = self.request.get('verify')
        user_email = self.request.get('email')
        
        username_test = self.valid_username(user_username)
        password_test = self.valid_password(user_password)
        verify_test = self.text_match(user_password,user_verify)
        email_test = self.valid_email(user_email)
        available = self.available_username(user_username)



        username_error= ""
        password_error= ""
        verify_error= ""
        email_error=""
        

        if user_email == "":
            if (username_test and password_test and verify_test and available):

                e = User(key_name= user_username, username = user_username, password=make_pw_hash(user_username,user_password))
            
                e.put()

                self.redirect('/blog/welcome')

                
                self.set_secure_cookie('user_id', str(user_username))
                
              

            else:
                if not username_test:
                    username_error = "Wrong username"

                if not password_test:
                        password_error ="Invalid password"
                else:
                    if not verify_test:
                        verify_error = "Passwords don't match"
                    if not available:
                        username_error ="Username is not available"

                self.render("signup.html",username=user_username,username_error=username_error,password="",password_error=password_error,
                       verify="",verify_error=verify_error,email=user_email,email_error=email_error)

        else:
            if (username_test and password_test and verify_test and email_test and available):
                e = User(username=user_username, password=make_pw_hash(user_usename,user_password),email=user_email)
            
                e.put()


                self.redirect('/blog/welcome')

                self.set_secure_cookie('user_id', str(user_username))

            else:
                if not email_test:
                    email_error = "invalid email"

                if not username_test:
                    username_error = "Wrong username"
                if not verify_test :
                    verify_error = "Passwords don't match"
                if not available:
                    username_error ="Username is not available"
                else:
                    if not password_test:
                        password_error ="Invalid password"

                self.render("signup.html", username=user_username,username_error=username_error,password="",password_error=password_error,
                       verify="",verify_error=verify_error,email=user_email,email_error=email_error)
class Login(SignUp):


    def get(self):
        #self.response.headers['Content-Type'] ='text/plain'
        self.render("login.html",username="",username_error="",password="",password_error="")

    def post(self):
        user_username = self.request.get('username')
        user_password = self.request.get('password')
        user = User.get_by_key_name (user_username, parent=None)
        if user:
            if user.username == user_username and valid_pw(user_username, user_password, user.password):
                self.redirect('/blog/welcome')
                self.set_secure_cookie('user_id', str(user_username))
        else:
            self.render("login.html",username=user_password,username_error="Invalid Login")

class Logout(BaseHandler):
    def get(self):
        #self.response.headers['Content-Type'] ='text/plain'
        

        self.response.headers.add_header('Set-Cookie', 'username=''; Path=/')
        self.redirect('/blog/signup')



class WelcomeHandler(SignUp):
    def get(self):
    
        user = self.request.cookies.get('user_id')
        username = check_secure_val(user)
        
        self.render("welcome.html",username=username)   

class JsonHandler(BaseHandler):
    #get the page  in the handline
    
    #write to a string in Json

    #render to page
    def render(self, thing):

        self.response.headers['Content-Type'] = 'application/json'   

        self.response.out.write(thing)

    def get(self):
        entries = db.GqlQuery("SELECT * FROM Entry ORDER BY created  DESC")
        #p = json.dumps(entries)
        output = []
        for entry in entries:
            dictToAdd ={}
            dictToAdd["content"]= entry.entry
            dictToAdd["subject"]= entry.title
            output.append(dictToAdd)

        self.render(json.dumps(output))



class JsonHandlerPerma(JsonHandler):
    def get(self,product_id):
        ID=int(product_id)
        entry = db.GqlQuery("SELECT * FROM Entry where __key__ = KEY('Entry', %s)" %ID)

         
        #p = json.dumps(entries)
        output = []
       
        dictToAdd ={}
        dictToAdd["content"]= entry[0].entry
        dictToAdd["subject"]= entry[0].title
        self.render(json.dumps(dictToAdd))

class Flush(BaseHandler):
    def get(self):
        memcache.flush_all()
        #self.redirect("/blog/")











app = webapp2.WSGIApplication([
    ('/', MainHandler),
    ('/container', LoadPlan),
    ('/clear', Clear),
    ('/blog/flush', Flush),
    ('/blog/newpost', NewPost),
    ('/blog/signup', SignUp),
    ('/blog/?', Blog),
    ('/blog/.json', JsonHandler),
    ('/blog/welcome', WelcomeHandler),
    ('/blog/entries/(\d+)', Entries),
    ('/blog/entries/(\d+).json', JsonHandlerPerma),
    ('/blog/login', Login),
    ('/blog/logout', Logout)], debug=True)
