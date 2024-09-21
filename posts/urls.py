from django.urls import path

from posts.views import PostDetail, PostList, UserList, UserDetail


urlpatterns = [
    path("", PostList.as_view(), name="post_list"),
    path("users/", UserList.as_view(), name="user_list"),
    path("<int:pk>/", PostDetail.as_view(), name="post_detail"),
    path("users/<int:pk>/", UserDetail.as_view(), name="user_detail"),
]
