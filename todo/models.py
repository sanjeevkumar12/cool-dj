from django.db import models
import itertools
from django.utils.translation import gettext_lazy as __
from django.conf import settings
from django.utils.text import slugify
class TaskList(models.Model):
    title = models.CharField(__('Task List Name'),max_length=244,db_index=True)
    description = models.TextField(__('List Description'),max_length=500)
    user = models.ForeignKey(settings.AUTH_USER_MODEL)
    slug = models.SlugField(max_length=254,db_index=True,unique= True,blank=True)
    created = models.DateTimeField(__('Created'),auto_now_add=True)

    def save(self,force_insert=False, force_update=False, using=None,update_fields=None):
        if not self.slug:
            lenslug = 200
            if not len(self.title) > 200:
                lenslug = len(self.title)
            self.slug = slugify(self.title)[0:lenslug]
            for x in itertools.count(1):
                if not TaskList.objects.filter(slug=self.slug).exists():
                    break
                self.slug = "%s-%d" % (slugify(self.title)[0:lenslug],x)
        super(TaskList,self).save(force_insert=False, force_update=False, using=None,update_fields=None)
    def __str__(self):
        return self.title
    class Meta:
        unique_together = ('title','user')
class TodoItem(models.Model):

    DRAFT = 0
    PENDING  = 1
    INPRORESS =  2
    COMPLETE = 3
    ONHOLD = 4

    PNORMAL = 0
    PMEDIUM = 1
    PHIGH = 2
    PCRITICAL  = 3

    PRIORITYLEVELS = (
                (PNORMAL ,__('Normal')),
                (PMEDIUM ,__('Medium')),
                (PHIGH ,__('High')),
                (PCRITICAL ,__('Critial'))
            )

    STATUS = (
        (DRAFT,__('Draft')),
        (PENDING,__('Pending')),
        (INPRORESS,__('In-Progress')),
        (COMPLETE,__('Complete')),
        (ONHOLD,__('On-Hold')),
    )
    title = models.CharField(__('Task Name'),max_length=244,db_index=True)
    description = models.TextField(__('Description'),max_length=500)
    status = models.IntegerField(__('Task Status'),choices=STATUS,default=PENDING)
    priority = models.IntegerField(__('Priority'),choices=PRIORITYLEVELS,default=PNORMAL)
    todolist = models.ForeignKey(TaskList)
    duedatetime = models.DateTimeField(__('Due Date'),blank=True)
    slug = models.SlugField(max_length=254,db_index=True,blank=True )
    created = models.DateTimeField(__('Created'),auto_now_add=True)
    modified = models.DateTimeField(__('Last Modified'),auto_now=True)

    def save(self,force_insert=False, force_update=False, using=None,update_fields=None):
        if not self.slug:
            lenslug = 200
            if not len(self.title) > 200:
                lenslug = len(self.title)
            self.slug = slugify(self.title)[0:lenslug]
            for x in itertools.count(1):
                if not TodoItem.objects.filter(slug=self.slug).exists():
                    break
                self.slug = "%s-%d" % (slugify(self.title)[0:lenslug],x)
        super(TodoItem,self).save(force_insert=False, force_update=False, using=None,update_fields=None)
    def __str__(self):
        return self.title

    class Meta:
        unique_together = ('title','todolist')
