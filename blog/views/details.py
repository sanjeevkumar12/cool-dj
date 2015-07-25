from django.views.generic import DetailView,ListView
from ..models import Post,Category
from .mixin import BlogMixin
class SlugDetailView(BlogMixin,DetailView):
    model = Post
    template_name = 'blog/post-detail.html'

    def get_object(self, queryset=None):
        try:
            return Post.objects.published().filter(slug=self.kwargs.get('slug')).get()
        except Post.DoesNotExist:
            return None
    def render_to_response(self, context, **response_kwargs):
        return super(SlugDetailView,self).render_to_response( context, **response_kwargs)

class CategoryDetailView(ListView):
    model = Post

    def get_object(self,queryset=None):
        try:
            return Category.objects.filter(slug=self.kwargs.get('slug'))
        except Category.DoesNotExist:
            return None