from django.contrib import admin
from .models import Post,BlogConfig,Category,Tag
from django_markdown.widgets import AdminMarkdownWidget
from django.db.models import TextField
from django_markdown.admin import MarkdownModelAdmin
from django.forms import forms
from django.db import models

from django.contrib.admin import SimpleListFilter

class CategoryListFilter(SimpleListFilter):
    title = "category"
    parameter_name = "category"
    def lookups(self, request, model_admin):
        categories = Category.objects.all()
        for category in categories:
            yield (category.pk,category.title)
    def queryset(self, request, queryset):
        if self.value():
            return queryset.filter(category__pk = self.value)

class BlogPostAdmin(MarkdownModelAdmin):
    list_display = ("title",'created','modified','status',)
    prepopulated_fields = {"slug": ("title",)}
    list_filter = (CategoryListFilter, 'status', )
    filter_vertical  = ('category','tags',)
    formfield_overrides = { models.TextField: {'widget': forms.Textarea(attrs={'class':'ckeditor'})}, }
    fieldsets = [
                    (None,{'fields':['title','slug',]}),
                    ('Blog Content',{'fields':['shortdescription','content',]}),
                    ('Blog Settings',{'fields':['accesstype','commentenabled',]}),
                    ('Additional Inf',{'fields':['category','tags','author',]}),

            ]
    class Media:
        js = ('assets/ckeditor/ckeditor.js',)

    actions = ['make_published','make_archived','make_pending', ]


    def category(self,object):
        return object.category.pk

    def tag(self,object):
        return object.tag.pk

    def author(self,object):
        return object.author.pk

    def get_actions(self, request):
        actions = super(BlogPostAdmin, self).get_actions(request)
        if 'delete_selected' in actions:
            del actions['delete_selected']
        return actions

    def make_published(self, request, queryset):
        queryset.update(status=Post.PENDING)
    def make_archived(self, request, queryset):
        queryset.update(status=Post.DELETED)
    def make_pending(self, request, queryset):
        queryset.update(status=Post.PENDING)
    make_published.short_description = "Mark selected post as Published"
    make_pending.short_description = "Mark selected post as Pending"
    make_archived.short_description = "Mark selected post as Archived"

admin.site.register(Post,BlogPostAdmin)
admin.site.register(Category)
admin.site.register(BlogConfig)
admin.site.register(Tag)