from django.urls import path

from .views import detail_post, render_post

app_name = 'blog'

urlpatterns = [
    path('',render_post, name = "posts"),
    path("<int:posts_id>", detail_post , name = "detail_post" )
]