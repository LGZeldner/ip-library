from django.contrib import admin
from core.models import Books, Book_types, Book_authors, Book_tags, Baccess, Busers, bgroups, ref_userAccess, ref_userGroup, ref_groupAccess, ref_bookAuthor, ref_bookTags

@admin.register(Books)
class BooksAdmin(admin.ModelAdmin):
    list_display = ("name", "type_id")
    pass

@admin.register(Book_types)
class Book_typesAdmin(admin.ModelAdmin):
    pass

@admin.register(Book_authors)
class Book_authorsAdmin(admin.ModelAdmin):
    list_display = ("fname", "mname", "lname")
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
    pass

@admin.register(bgroups)
class bgroupsAdmin(admin.ModelAdmin):
    pass
    
@admin.register(ref_userAccess)
class ref_userAccessAdmin(admin.ModelAdmin):
    list_display = ("user_id", "access_id")
    pass

@admin.register(ref_userGroup)
class ref_userGroupAdmin(admin.ModelAdmin):
    list_display = ("user_id", "group_id")
    pass
    
@admin.register(ref_groupAccess)
class ref_groupAccessAdmin(admin.ModelAdmin):
    list_display = ("group_id", "access_id")
    pass

@admin.register(ref_bookAuthor)
class ref_bookAuthorAdmin(admin.ModelAdmin):
    list_display = ("book_id", "author_id")
    pass

@admin.register(ref_bookTags)
class ref_bookTagsAdmin(admin.ModelAdmin):
    list_display = ("book_id", "tag_id")
    pass

    