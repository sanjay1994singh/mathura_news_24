from django.shortcuts import render

from post.models import Post


# Create your views here.
def detail(request, id):
    post = Post.objects.get(id=id)
    featured_image_url = post.featured_image.url
    count = post.count + 1
    post.count = count
    post.save()

    absolute_image_url = request.build_absolute_uri(featured_image_url)
    context = {
        'news': post,
        'absolute_image_url': absolute_image_url,
    }
    return render(request, 'details.html', context)
