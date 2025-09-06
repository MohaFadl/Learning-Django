from django.shortcuts import get_object_or_404, render
from django.http import Http404
from .models import Post
from django.core.paginator import Paginator , EmptyPage

def post_list(request):
    posts_list = Post.published.all()
    paginator = Paginator(posts_list,3)
    page_number = request.GET.get('page' , 1)
    try:
        posts = paginator.get_page(page_number)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)

    return render(
        request,
        'blog/post/list.html',
        {'posts':posts}
    )

def post_detail (request , year , month , day , post):

    post = get_object_or_404(
        Post,
        status=Post.Status.PUBLISHED,
        slug=post,
        publish__year=year,
        publish__month=month,
        publish__day=day
    )
    return render(
        request,
        'blog/post/details.html',
        {'post':post}
    )




