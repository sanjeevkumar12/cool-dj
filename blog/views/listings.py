from ..models import Post,Category,PostComment,Tag
from django.views.generic import ListView,RedirectView
from django.db.models import Count
from .mixin import BlogMixin
from django.db.models import Q
from django.core.urlresolvers import reverse_lazy
from  django.views.generic import FormView
from django.shortcuts import redirect
class PostList(BlogMixin,ListView):
    model = Post
    template_name = "blog/listing.html"
    def get_queryset(self):
        return Post.objects.published().select_related().annotate(comment_count=Count('postcomment'))

class TagPostListing(BlogMixin,ListView):
    model = Post
    template_name = "blog/tagpostslist.html"

    def get_queryset(self):
        return Post.objects.filter(tags__slug=self.kwargs['tagslug']).select_related().annotate(comment_count=Count('postcomment'))


class AjaxCommentList(ListView):

    def get_queryset(self):
        return PostComment.objects.filter(approved=True).select_related()

class AddSearch(FormView):
    def post(self, *args, **kwargs):
        return redirect(reverse_lazy('blog:search',{'keyword': self.request.POST['search']}))
class SearchList(BlogMixin,ListView):
    model = Post
    template_name = "blog/listing.html"
    def get_queryset(self):
        return Post.objects.published().filter(
                            Q(title__icontains=self.kwargs.get('keyword')) |
                            Q(category__title__exact=self.kwargs.get('keyword')) |
                            Q(tags__title__exact=self.kwargs.get('keyword'))
                    ).select_related().annotate(comment_count=Count('postcomment'))
