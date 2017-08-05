from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import View
from django.http import HttpResponseRedirect

from django.views.decorators.http import require_http_methods

from .models import Post

def redirect_root(request):
    return redirect('blog_post_list')

class PostList(View):
    # template_name = 'blog/post_list.html'
    def get(self, request):
        return render(request, 'blog/post_list.html', {'post_list':Post.objects.all()})


# def post_lisft(request):
#     return render(request, 'blog/post_list.html', {'post_list': Post.objects.all()})

@require_http_methods(['HEAD','GET'])
def post_detail(request, year, month, slug):
    post = get_object_or_404(Post,
                             pub_date__year=year,
                             pub_datE__month=month,
                             slug=slug)
    return render(request, 'blog/post_detail.html', {'post':post})