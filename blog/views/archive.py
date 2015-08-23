from django.views.generic import YearArchiveView,MonthArchiveView,DayArchiveView
from ..models import Post
from ..views.mixin import BlogMixin

class YearlyView(BlogMixin,YearArchiveView):

    date_field = 'publisheddate'
    template_name = 'blog/listing.html'
    queryset = Post.objects.published().select_related()
    model = Post
    make_object_list = True
    allow_future = False

class MonthlyView(BlogMixin,MonthArchiveView):
    date_field = 'publisheddate'
    template_name = 'blog/listing.html'
    queryset = Post.objects.published().select_related()
    model = Post
    make_object_list = True
    allow_future = False
    month_format = '%B'


class DateView(BlogMixin,DayArchiveView):
    date_field = 'publisheddate'
    template_name = 'blog/listing.html'
    queryset = Post.objects.published().select_related()
    model = Post
    make_object_list = True
    allow_future = False
