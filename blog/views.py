from django.shortcuts import render, get_object_or_404
from .models import Posts

def render_post(request):
    articles = Posts.objects.all()
    return render(request, 'posts.html', {'articles' : articles})


def detail_post(request, posts_id):
    article = get_object_or_404(Posts, pk = posts_id )
    return render (request, 'post_detail.html', {'article': article})