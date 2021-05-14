from django.shortcuts import render

from rest_framework import viewsets

from .serializers import BooksSerializer, Book_typesSerializer
from core.models import Books, Book_types, Book_authors, Book_tags, Baccess, Busers, bgroups, ref_userAccess, ref_userGroup, ref_groupAccess, ref_bookAuthor, ref_bookTags


class BooksViewSet(viewsets.ModelViewSet):
    queryset = Books.objects.all().order_by('name')
    serializer_class = BooksSerializer

class Book_typesViewSet(viewsets.ModelViewSet):
    queryset = Book_types.objects.all().order_by('name')
    serializer_class = Book_typesSerializer