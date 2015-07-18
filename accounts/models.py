from django.db import models
from django.core.urlresolvers import reverse
from django.contrib.auth.models import AbstractBaseUser,PermissionsMixin,BaseUserManager
from django.utils.text import slugify
import itertools
from django.utils.translation import ugettext_lazy as __
from PIL import Image as PImage
import hashlib,datetime,random
from  django.core.mail import send_mail,EmailMessage
from django.template.loader import get_template
from django.template import Context
from Inventory.utils import String
from django.utils import timezone
class UserManager(BaseUserManager):
    def create_user(self,email,password):
        if not email :
            raise ValueError(__('User must have a email address'))
        user = self.model(email=self.normalize_email(email))
        user.is_active = True
        user.set_password(password)
        user.save(using = self._db)
        return user
    def create_superuser(self,email,password):
        user = self.create_user(email,password)
        user.is_staff = True
        user.is_superuser = True
        user.save(using = self._db)
        return user


class User(AbstractBaseUser,PermissionsMixin):
    ACTIVATION_LINK_EXPIRE = 10

    email = models.EmailField(__('Email Address'),unique=True,db_index=True)
    firstname = models.CharField(__('First Name'),blank=True,null=True,max_length=20)
    lastname = models.CharField(__('Last Name'),blank=True,null=True,max_length=20)
    user_bio = models.TextField(__('User Intro'),blank=True,null=True)
    slug = models.SlugField(max_length=254,db_index=True,unique= True,blank=True)
    user_hash = models.CharField(max_length=254,default='',blank=True)
    hash_expire = models.DateTimeField(auto_now_add=True,blank=True)
    is_staff = models.BooleanField(__('Is staff user'),default=False)
    is_active = models.BooleanField(__('Active'),default=False)
    date_joined = models.DateTimeField(__('Joined Time'),auto_now_add=True)
    image = models.ImageField(__('User Image'),upload_to='uploads/users/profile/',blank=True,null=True,default='uploads/users/profile/noimage.png')
    avatar = models.ImageField(__('User Image'),upload_to='uploads/users/avatar/',blank=True,null=True,default='uploads/users/avatar/noimage.png')

    objects = UserManager()

    def get_full_name(self):
        return '{0} {1}'.format(self.firstname,self.lastname)
    def __str__(self):
        return '{0} {1}'.format(self.firstname,self.lastname)
    def get_short_name(self):
        return '{0}'.format([self.firstname,])
    def __unicode__(self):
        return '{0} {1}'.format(self.firstname,self.lastname)

    def save(self,force_insert=False, force_update=False, using=None,update_fields=None):
        if not self.slug:
            lenslug = 210
            if self.firstname:
                sludata = self.firstname + ' ' + self.lastname
            else:
                sludata = self.email
            if not len(sludata) > 210:
                lenslug = len(sludata)
            self.slug = slugify(sludata)[0:lenslug]
            for x in itertools.count(1):
                if not User.objects.filter(slug=self.slug).exists():
                    break
                self.slug = "%s-%d" % (slugify(self.slug),x)
        super(User,self).save(force_insert=False, force_update=False, using=None,update_fields=None)

    def sendactivationmail(self,request):
        self.user_hash = String.createhashforstring(self.email)
        self.hash_expire = datetime.datetime.today() + datetime.timedelta(User.ACTIVATION_LINK_EXPIRE)
        self.save()
        email_subject = __('Account confirmation')
        confirmurl = reverse("accounts:emailconfirmation", kwargs={'userslug': self.slug,'activationkey':self.user_hash,})
        data = {
            'firstname':self.firstname,
            'lastname':self.lastname,
            'userslug':self.slug,
            'userhash':self.user_hash,
            'request':request,
            'verifyurl':request.build_absolute_uri(confirmurl)
        }
        message = get_template('accounts/email/regconfirm.html').render(Context(data))
        email = EmailMessage(email_subject,message,'sanjumassal@gmail.com',['sanjeev.kumar.12@netsolutionsindia.com'])
        email.content_subtype = 'html'
        email.send()



    USERNAME_FIELD = 'email'
    class Meta:
        verbose_name = __('user')
        verbose_name_plural = __('users')
        app_label = 'accounts'

