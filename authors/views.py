from django.shortcuts import render
from .forms import *
from .models import *

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


    author = Author.objects.filter()


    return render(request, 'authors/author.html',{"authors":  author}, locals())




def tag(request):
    form = AuthorForm(request.POST or None)

    if request.method == "POST" and form.is_valid():
        print(request.POST)
        print(form.cleaned_data)
        data = form.cleaned_data


        new_form = form.save()





    return render(request, 'authors/tag.html', locals())