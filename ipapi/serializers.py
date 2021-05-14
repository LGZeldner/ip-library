from rest_framework import serializers

from core.models import Books, Book_types, Book_authors, Book_tags, Baccess, Busers, bgroups, ref_userAccess, ref_userGroup, ref_groupAccess, ref_bookAuthor, ref_bookTags


class BooksSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Books
        fields = ('type', 'name', 'book')

class Book_typesSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Book_types
        fields = ('name')