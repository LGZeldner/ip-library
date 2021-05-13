from django.contrib import admin
from core.models import Books, Book_types, Book_authors, Book_tags, Baccess, Busers, bgroups, ref_userAccess, ref_groupAccess, ref_bookAuthor, ref_bookTags

@admin.register(Books)
class BooksAdmin(admin.ModelAdmin):
    pass

@admin.register(Book_types)
class Book_typesAdmin(admin.ModelAdmin):
    pass

@admin.register(Book_authors)
class Book_authorsAdmin(admin.ModelAdmin):
    pass

@admin.register(Book_tags)
class Book_tagsAdmin(admin.ModelAdmin):
    pass
    
@admin.register(Baccess)
class BaccessAdmin(admin.ModelAdmin):
    pass

@admin.register(Busers)
class BusersAdmin(admin.ModelAdmin):
    pass

@admin.register(bgroups)
class bgroupsAdmin(admin.ModelAdmin):
    pass
    
@admin.register(ref_userAccess)
class ref_userAccessAdmin(admin.ModelAdmin):
    pass

@admin.register(ref_groupAccess)
class ref_groupAccessAdmin(admin.ModelAdmin):
    pass

@admin.register(ref_bookAuthor)
class ref_bookAuthorAdmin(admin.ModelAdmin):
    pass

@admin.register(ref_bookTags)
class ref_bookTagsAdmin(admin.ModelAdmin):
    pass

    