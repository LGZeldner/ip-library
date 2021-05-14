from django.shortcuts import render

from rest_framework import viewsets

from .serializers import BooksSerializer, Book_typesSerializer, Book_authorsSerializer, Book_tagsSerializer
from core.models import Books, Book_types, Book_authors, Book_tags


class BooksViewSet(viewsets.ModelViewSet):
    queryset = Books.objects.all().order_by('name')
    serializer_class = BooksSerializer

class Book_typesViewSet(viewsets.ModelViewSet):
    queryset = Book_types.objects.all().order_by('name')
    serializer_class = Book_typesSerializer

class Book_authorsViewSet(viewsets.ModelViewSet):
    queryset = Book_authors.objects.all().order_by('lname')
    serializer_class = Book_authorsSerializer

class Book_tagsViewSet(viewsets.ModelViewSet):
    queryset = Book_tags.objects.all().order_by('name')
    serializer_class = Book_tagsSerializer