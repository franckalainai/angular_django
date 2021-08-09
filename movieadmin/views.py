from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from .models import Book


class Another(View):
    book = Book.objects.get(id=2)
    output = f"we have {book.title} book with ID {book.id} in our database"

    def get(self, request):
        return HttpResponse(self.output)


def first(request):
    return HttpResponse('Fisrt message from views')
