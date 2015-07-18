from django.views.generic import DetailView,ListView
from ..models import Post,Category
class SlugDetailView(DetailView):
    model = Post

    def get_object(self, queryset=None):
        try:
            return Post.objects.published().filter(slug=self.kwargs.get('slug'))
        except Post.DoesNotExist:
            return None

class CategoryDetailView(ListView):
    model = Post

    def get_object(self,queryset=None):
        try:
            return Category.objects.filter(slug=self.kwargs.get('slug'))
        except Category.DoesNotExist:
            return None