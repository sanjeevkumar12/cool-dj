import hmac
import random
import string
import hashlib

class String(object):

    """

            salt = str(random.random()).encode('utf-8')
            salt =  hashlib.sha1(salt).hexdigest() + self.email +  hashlib.sha1(salt).hexdigest()[5:10]
            lenslug = 210
            self.user_hash = hashlib.sha1(salt.encode('utf-8')).hexdigest()
            self.hash_expire = datetime.datetime.today() + datetime.timedelta(10)
    """


    @staticmethod
    def generatesalt():
        salt = hashlib.sha1(str(random.random()).encode('utf-8'))
        return salt.hexdigest()

    @staticmethod
    def createhashforstring(string):
        salt = String.generatesalt()
        salt =  salt[0:5] + string +  salt[0:5]
        return hashlib.sha1(salt.encode('utf-8')).hexdigest()