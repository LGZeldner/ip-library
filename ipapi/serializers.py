#Serializers for JSON
from rest_framework import serializers

from core.models import Books, Book_types, Book_authors, Book_tags


class BooksSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Books
        fields = ('type', 'name', 'book',)

class Book_typesSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Book_types
        fields = ('name',)

class Book_authorsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Book_authors
        fields = ('fname', 'mname', 'lname',)

class Book_tagsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Book_tags
        fields = ('name',)        