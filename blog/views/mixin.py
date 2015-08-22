from django.views.generic.base import TemplateResponseMixin
from ..models import Category,Post,Tag
from .viewhelpers import Archive



class BlogMixin(TemplateResponseMixin):
    def render_to_response(self, context, **response_kwargs):
        categories = Category.objects.extra(select={'liveposts':"SELECT count(*) from blog_post_category LEFT JOIN blog_post ON (blog_post.id = blog_post_category.post_id) WHERE blog_post.status = 2 AND blog_post_category.category_id = blog_category.id"}).all()
        context['categories'] = categories
        context['recentposts'] = Post.objects.recent().select_related()[:5]
        context['tags'] = Tag.objects.all()
        context['list_events'] = Archive.getarchivelist()
        return super(BlogMixin,self).render_to_response(context, **response_kwargs)
