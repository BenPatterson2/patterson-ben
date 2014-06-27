
import hashlib
import hmac

secret = 'blah_blah_blah'

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

