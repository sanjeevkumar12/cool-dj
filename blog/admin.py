from django.contrib import admin
from .models import Post,BlogConfig,Category,Tag
from django_markdown.widgets import AdminMarkdownWidget
from django.db.models import TextField
from django_markdown.admin import MarkdownModelAdmin

class BlogPostAdmin(MarkdownModelAdmin):
    list_display = ("title", "created")
    prepopulated_fields = {"slug": ("title",)}
    formfield_overrides = {TextField: {'widget': AdminMarkdownWidget}}

    actions = ['make_published','make_archived','make_pending', ]

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

