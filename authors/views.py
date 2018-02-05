from django.shortcuts import render
from .forms import *
from .models import *
from django.shortcuts import render, get_object_or_404
from django.shortcuts import redirect
from django.utils import timezone
def authors(request):

    # name = "CodingMedved"
    # current_day = "03.01.2017"
    # form = SubscriberForm(request.POST or None)
    #
    # if request.method == "POST" and form.is_valid():
    #     print (request.POST)
    #     print (form.cleaned_data)
    #     data  = form.cleaned_data
    #     print (data["name"])
    #
    #     new_form = form.save()


    author = Author.objects.all()


    return render(request, 'authors/author.html',{"authors":  author})




def tag(request):
    form = AuthorForm(request.POST or None)

    if request.method == "POST" and form.is_valid():
        print(request.POST)
        print(form.cleaned_data)
        data = form.cleaned_data


        new_form = form.save()





    return render(request, 'authors/tag.html', locals())


def author_edit(request, pk):
    author = get_object_or_404(Author, pk=pk)
    if request.method == "POST":
        form = AuthorForm(request.POST, instance=author)
        if form.is_valid():
            author = form.save(commit=False)
            author.author = request.user
            author.published_date = timezone.now()
            author.save()


    else:
        form = AuthorForm(instance=author)
    return render(request, 'authors/tag.html', locals())

