from django.contrib import admin
from .models import Post,BlogConfig,Category
from django_markdown.widgets import AdminMarkdownWidget
from django.db.models import TextField
from django_markdown.admin import MarkdownModelAdmin

class BlogPostAdmin(MarkdownModelAdmin):
    list_display = ("title", "created")
    prepopulated_fields = {"slug": ("title",)}
    formfield_overrides = {TextField: {'widget': AdminMarkdownWidget}}

admin.site.register(Post,BlogPostAdmin)
admin.site.register(Category)
admin.site.register(BlogConfig)

