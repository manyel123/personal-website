from django.urls import path

from . import views 

urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register_view, name="register"),
    path("create_post", views.create_post_view, name="create_post"),
    path("delete_post", views.delete_post_view, name="delete_post"),
    path("edit_post", views.edit_post_view, name="edit_post"),
    path("create_comment", views.create_comment_view, name="create_comment"),
    path("delete_comment", views.delete_comment.views, name="delete_comment"),
]