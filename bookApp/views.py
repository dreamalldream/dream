from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

from .models import Book


def index(request):
    booklist = Book.objects.all()
    return render(request, 'book/index.html', {'booklist': booklist})
    # return HttpResponse("图书管理系统")
def detail(request, id):
    book = Book.objects.get(pk=id)
    return render(request, 'book/detail.html', {'book': book})
    # return HttpResponse("图书管理详情页信息 %s" % id)