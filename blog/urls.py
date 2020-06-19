from django.urls import path

from . import views

app_name = "blog"

urlpatterns = [
    path('', views.PostListView.as_view(), name='PostList'),
    path("<int:pk>/", views.PostPage.as_view(), name="PostPage"),
]
