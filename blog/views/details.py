from django.views.generic import DetailView
from ..models import Post
class SlugDetailView(DetailView):
    model = Post

    def get_queryset(self):
        try:

        except Post.DoesNotExist:
            return None