from django.contrib import admin
from django.urls import reverse
from django.utils.http import urlencode
from core.models import Books, Book_types, Book_authors, Book_tags, Baccess, Busers, bgroups, ref_userAccess, ref_userGroup, ref_groupAccess, ref_bookAuthor, ref_bookTags

@admin.register(Books)
class BooksAdmin(admin.ModelAdmin):
    list_display = ("name", "type")
    list_filter = ["type"]
    search_fields = ("name__startswith", )
    pass

@admin.register(Book_types)
class Book_typesAdmin(admin.ModelAdmin):
    pass

@admin.register(Book_authors)
class Book_authorsAdmin(admin.ModelAdmin):
    list_display = ("fname", "mname", "lname")
    search_fields = ("lname__startswith", )
    pass

@admin.register(Book_tags)
class Book_tagsAdmin(admin.ModelAdmin):
    pass
    
@admin.register(Baccess)
class BaccessAdmin(admin.ModelAdmin):
    pass

@admin.register(Busers)
class BusersAdmin(admin.ModelAdmin):
    list_display = ("name", "login", "email")
    search_fields = ("login__startswith", )
    pass

@admin.register(bgroups)
class bgroupsAdmin(admin.ModelAdmin):
    pass
    
@admin.register(ref_userAccess)
class ref_userAccessAdmin(admin.ModelAdmin):
    list_display = ("user", "access")
    list_filter = ["access"]
    pass

@admin.register(ref_userGroup)
class ref_userGroupAdmin(admin.ModelAdmin):
    list_display = ("user", "group")
    list_filter = ["group"]
    pass
    
@admin.register(ref_groupAccess)
class ref_groupAccessAdmin(admin.ModelAdmin):
    list_display = ("group", "access")
    pass

@admin.register(ref_bookAuthor)
class ref_bookAuthorAdmin(admin.ModelAdmin):
    list_display = ("book", "author")
    list_filter = ["author"]
    pass

@admin.register(ref_bookTags)
class ref_bookTagsAdmin(admin.ModelAdmin):
    list_display = ("book", "tag")
    list_filter = ["tag"]
    pass

    