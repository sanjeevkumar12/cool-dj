from django.db import models
from django.utils.text import slugify
from django.core.urlresolvers import reverse_lazy
from django.utils.translation import ugettext_lazy as __
from django.conf import settings
from django.utils import timezone

class BlogConfig(models.Model):
    commentson = models.BooleanField(default=True)

class Category(models.Model):
    title = models.CharField(__('Category title'),max_length=200,unique=True,db_index=True)
    description = models.TextField(__("Category Detail"),max_length=500,blank=True,default='')
    created = models.DateTimeField(__("Created On"),auto_now_add=True)
    modified = models.DateTimeField(__("Modified On"),auto_now=True)
    slug = models.SlugField(db_index= True,blank=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super(Category,self).save(*args, **kwargs)

    def __unicode__(self):
        return self.title

    def __str__(self):
        return self.title
    def get_absolute_url(self):
        return reverse_lazy('blog:blogdetail', kwargs={"slug": self.slug})

    class Meta:
        ordering = ["title"]
        db_table ="blog_category"
        verbose_name = __("Category")
        verbose_name_plural = __("Category")

class Tag(models.Model):
    title = models.CharField(__("Tag Name"),max_length=200,db_index=True,unique= True)
    description = models.TextField(__("Tag description"),max_length=400,blank=True,default='')
    created = models.DateTimeField(__("Created on"),auto_now_add=True)
    modified = models.DateTimeField(__("Last modified"),auto_now=True)
    slug = models.SlugField(db_index=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super(Tag,self).save(*args, **kwargs)

    def __unicode__(self):
        return self.title

    def __str__(self):
        return self.title

    class Meta:
        ordering = ["title"]
        db_table ="blog_tag"
        verbose_name = __("Tag")
        verbose_name_plural = __("Tag")


class PostManager(models.Manager):

    def published(self):
        return self.get_queryset().filter(status=2,publisheddate__lte=timezone.now())
    def upcoming(self):
        return self.get_queryset().filter(status=2,publisheddate__gt=timezone.now())
    def draft(self):
        return self.get_queryset().filter(status=0)
    def pending(self):
        return self.get_queryset().filter(status=1)
    def archived(self):
        return self.get_queryset().filter(status=3)
    def author(self,owner):
        return self.get_queryset().filter(status=2,author=owner)

class Post(models.Model):
    DRAFT = 0
    PENDING = 1
    PUBLISHED = 2
    DELETED = 3

    PUBLIC = 0
    PRIVATE = 1

    STATUS = (
        (DRAFT,__('Draft')),
        (PENDING,__('Pending')),
        (PUBLISHED,__('Published')),
        (DELETED,__('Archived')),
    )

    ACCESS = (
        (PUBLIC,"Publically Accessible"),
        (PRIVATE,"Limited Access"),
    )

    title = models.CharField(__("Post title"),max_length=240,db_index=True,unique=True)
    shortdescription = models.TextField(__("Short Introduction"),max_length=400,)
    content = models.TextField(__("Post HTML content"))
    status = models.SmallIntegerField(__("Post publish status"),choices=STATUS,default=DRAFT)
    accesstype = models.SmallIntegerField(__("Post public access "),choices=ACCESS,default=PUBLIC)
    author = models.ForeignKey(settings.AUTH_USER_MODEL)
    commentenabled = models.BooleanField(default= True)
    category = models.ManyToManyField(Category)
    publisheddate = models.DateTimeField(__("Published Date "),null =True,blank=True)
    slug = models.SlugField(null=True,blank=True)
    created = models.DateTimeField(__("Created on"),auto_now_add=True)
    modified = models.DateTimeField(__("Last Modified"),auto_now=True)


    objects = PostManager()
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super(Post,self).save(*args, **kwargs)


    def __unicode__(self):
        return self.title

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse_lazy("blog:postslugdetail", kwargs={"slug": self.slug})
    def markpublish(self):
        self.status = Post.PUBLISHED
        self.publisheddate = timezone.now()
        self.save()
    def markarhived(self):
        self.status = Post.DELETED

    def previous(self):
        try:
            return self.objects.published().filter(publisheddate__lte = timezone.now())[0]
        except self.DoesNotExist:
            return None
    def next(self):
        try:
            return self.objects.published().filter(publisheddate__gte = timezone.now())[0]
        except self.DoesNotExist:
            return None

    @property
    def is_public(self):
        if self.accesstype == Post.PUBLIC:
            return True
        return False

    class Meta:
        ordering = ["-created"]
        db_table ="blog_post"
        verbose_name = __("Post")
        verbose_name_plural = __("Posts")
        get_latest_by = "publisheddate"


class PostMetta(models.Model):
    metakey = models.CharField(max_length=200)
    metavalue = models.TextField(max_length=500)
    post = models.ForeignKey(Post)

    class Meta:
        ordering = ["metakey"]
        db_table ="blog_post_metatags"
        verbose_name = __("Post Meta Tags")
        verbose_name_plural = __("Post Meta Tags")


class PostComment(models.Model):
    post = models.ForeignKey(Post)
    user = models.ForeignKey(settings.AUTH_USER_MODEL)
    content = models.TextField(__("Comment"))
    useripaddress = models.IPAddressField(default=False,blank=True)
    approved = models.BooleanField(default=False,blank=True)
    created = models.DateTimeField(auto_now_add=True)