from django.shortcuts import render


def tags(request):

    return render(request, 'tags/tag.html', locals())