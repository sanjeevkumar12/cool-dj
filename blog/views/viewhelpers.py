import datetime
from ..models import Post
class Archive():
    @staticmethod
    def getarchivelist():
        posts = Post.objects.published().filter().order_by('-publisheddate')
        now = datetime.datetime.now()
        post_dict = {}
        for i in range(posts[0].publisheddate.year, posts[len(posts)-1].publisheddate.year-1, -1):
            post_dict[i] = {}
            for month in range(1,13):
                post_dict[i][month] = []
        for post in posts:
            post_dict[post.publisheddate.year][post.publisheddate.month].append(post)
        post_sorted_keys = list(reversed(sorted(post_dict.keys())))
        list_posts = []
        for key in post_sorted_keys:
            adict = {key:post_dict[key]}
            list_posts.append(adict)
        return list_posts
