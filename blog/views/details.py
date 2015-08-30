from django.views.generic import DetailView,ListView
from ..models import Post,Category,Tag
from .mixin import BlogMixin
from django.db.models import Count
from django.shortcuts import get_object_or_404
class SlugDetailView(BlogMixin,DetailView):
    model = Post
    template_name = 'blog/post-detail.html'

    def get_object(self, queryset=None):
        try:
            return Post.objects.published().filter(slug=self.kwargs.get('slug')).select_related().annotate(comment_count=Count('postcomment')).get()
        except Post.DoesNotExist:
            return None
    def render_to_response(self, context, **response_kwargs):
        return super(SlugDetailView,self).render_to_response( context, **response_kwargs)

class CategoryDetailView(BlogMixin,ListView):
    model = Post
    template_name = 'blog/categorypostlisting.html'

    def get_queryset(self):
        self.category = get_object_or_404(Category.objects.filter(slug=self.kwargs.get('slug')))
        return Post.objects.published().filter(category = self.category).select_related()


    def get_object(self,queryset=None):
        try:
            return Category.objects.filter(slug=self.kwargs.get('slug'))
        except Category.DoesNotExist:
            return None
    def get_context_data(self, **kwargs):
        context = super(CategoryDetailView,self).get_context_data(**kwargs)
        context.update({'category':self.category})
        return context

class TagDetailView(BlogMixin,ListView):
    model = Post
    template_name = 'blog/categorypostlisting.html'

    def get_queryset(self):
        self.tag = get_object_or_404(Tag.objects.filter(slug=self.kwargs.get('slug')))
        return Post.objects.published().filter(tags=self.tag).select_related()
    def get_context_data(self, **kwargs):
        context = super(TagDetailView,self).get_context_data(**kwargs)
        context.update({'tag':self.tag})
        return context




class AuthorView(BlogMixin,ListView):
    model = Post
    template_name = 'blog/listing.html'
    def get_queryset(self):
        return Post.objects.published().filter(author__slug=self.kwargs.get('slug')).select_related().annotate(comment_count=Count('postcomment'))