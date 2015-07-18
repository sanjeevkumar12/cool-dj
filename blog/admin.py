from django.contrib import admin
from .models import Post,BlogConfig,Category

admin.site.register(Post)
admin.site.register(Category)
admin.site.register(BlogConfig)

