from django.urls import path
from .views import ListarPostsListView, IndexBlogView

urlpatterns = [
    path('', IndexBlogView.as_view(), name="home"),
    path('listar/', ListarPostsListView.as_view(), name='listar_posts'),
]