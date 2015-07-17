from django.db import models
from django.utils.text import slugify
class Category(models.Model):
    title = models.CharField(max_length=200,unique=True,db_index=True)
    description = models.TextField(max_length=500,blank=True,default='')
    slug = models.SlugField(db_index= True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super(Category,self).save(*args, **kwargs)

    def __unicode__(self):
        return self.title

    def get_absolute_url(self):
        return self.slug