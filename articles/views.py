from django.shortcuts import render

from .models import Article, Tag


def articles_list(request):
    template = 'articles/news.html'
    object_list  = Article.objects.all().prefetch_related('scopes')
    context = {'object_list': object_list}

    return render(request, template, context)
