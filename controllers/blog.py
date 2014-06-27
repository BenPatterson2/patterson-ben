



class NewPost(BaseHandler):
     #renders the page to post items too. The front handler(Blog) inherits from this class
    
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
           

        self.render("blogs.html", title=title, entry=entry, error=error, entries=entries, cached=seconds,)







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

        self.render("blogs.html", entries =entries, cached = seconds)

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
        self.redirect("/blog/")




