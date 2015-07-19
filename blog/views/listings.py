from ..models import Post,Category,PostComment
from django.views.generic import ListView
from django.views.generic.base import TemplateResponseMixin
from django.db.models import Count

class BlogMixin(TemplateResponseMixin):
    def render_to_response(self, context, **response_kwargs):
        categories = Category.objects.extra(select={'liveposts':"SELECT count(*) from blog_post_category LEFT JOIN blog_post ON (blog_post.id = blog_post_category.post_id) WHERE blog_post.status = 2 AND blog_post_category.category_id = blog_category.id"}).all()
        context['categories'] = categories
        return super(BlogMixin,self).render_to_response(context, **response_kwargs)


class PostList(BlogMixin,ListView):
    model = Post
    template_name = "blog/listing.html"
    def get_queryset(self):
        return Post.objects.published().select_related().annotate(comment_count=Count('postcomment'))


class AjaxCommentList(ListView):

    def get_queryset(self):
        return PostComment.objects.filter(approved=True).select_related()

