from django.http import JsonResponse
from django.shortcuts import render

from post.models import Post


# Create your views here.
def homepage(request):
    try:
        post = Post.objects.all().order_by('-id')
        # top tranding news ----
        first_news = post[0]
        top_other_tranding = post[1:4]
        # end top tranding news ----

        crime_news = post.filter(category__name='Crime')[:5]
    except:
        pass
        first_news = ''
        top_other_tranding = ''
        crime_news = ''

    context = {
        'first_news': first_news,
        'other_top': top_other_tranding,
        'crime_news': crime_news,
    }
    return render(request, 'homepage.html', context)


def top_header_scroll(request):
    post = Post.objects.all().order_by('-id')[:4]
    news_list = []
    for i in post:
        data_dict = {}
        data_dict['id'] = i.id
        data_dict['title'] = i.title
        news_list.append(data_dict)
    context = {
        'news': news_list
    }
    return JsonResponse(context)
