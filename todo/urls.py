from django.conf.urls import url
from . import views
urlpatterns = [
        url(r'^$',views.TodoList.as_view(),name='listview'),
        url(r'^(?P<slug>[-\w]+)$',views.ToDoItemDetailView.as_view(),name='listdetail12'),
        url(r'^(?P<todolistslug>[-\w]+)/(?P<slug>[-\w]+)$',views.ToDoItemDetailView.as_view(),name='listdetail'),
    ]
