from ..models import Post,Category,PostComment,Tag
from django.views.generic import ListView
from django.db.models import Count
from .mixin import BlogMixin

class PostList(BlogMixin,ListView):
    model = Post
    template_name = "blog/listing.html"
    def get_queryset(self):
        return Post.objects.published().select_related().annotate(comment_count=Count('postcomment'))

class TagPostListing(BlogMixin,ListView):
    model = Post
    template_name = "blog/tagpostslist.html"

    def get_queryset(self):
        return Post.objects.filter(tags__slug=self.kwargs['tagslug'])


class AjaxCommentList(ListView):

    def get_queryset(self):
        return PostComment.objects.filter(approved=True).select_related()

