from django.contrib import admin
from django.urls import reverse
from django.utils.http import urlencode
from django.http import HttpResponseRedirect
from django.conf.urls import url

from import_export.admin import ImportExportModelAdmin
from import_export import resources


from core.models import Books, Book_types, Book_authors, Book_tags, Baccess, Busers, bgroups, ref_userAccess, ref_userGroup, ref_groupAccess, ref_bookAuthor, ref_bookTags

admin.site.site_header = 'Library on Django'

class BooksResource(resources.ModelResource):

    class Meta:
        model = Books
        skip_unchanged = True
        report_skipped = False
        fields = ('type', 'name', 'book')        
        export_order = ('name', 'type', 'book')

@admin.action(description="Revoke special status")
def make_general(modeladmin, request, queryset):
    queryset.update(access=1)


@admin.register(Books)
class BooksAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ("name", "type")
    list_filter = ["type"]
    search_fields = ("name__startswith", )
    resource_class = BooksResource
    pass


class Book_typesResource(resources.ModelResource):

    class Meta:
        model = Book_types
        skip_unchanged = True
        report_skipped = False
        fields = ('name') 
        
@admin.register(Book_types)
class Book_typesAdmin(ImportExportModelAdmin, admin.ModelAdmin): 
    resource_class = Book_typesResource
    pass

class Book_authorsResource(resources.ModelResource):

    class Meta:
        model = Book_authors
        skip_unchanged = True
        report_skipped = False
        fields = ("fname", "mname", "lname") 

@admin.register(Book_authors)
class Book_authorsAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ("fname", "mname", "lname")
    search_fields = ("lname__startswith", )
    resource_class = Book_authorsResource
    pass


class Book_tagsResource(resources.ModelResource):

    class Meta:
        model = Book_tags
        skip_unchanged = True
        report_skipped = False
        fields = ('name') 
@admin.register(Book_tags)
class Book_tagsAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    resource_class = Book_tagsResource
    pass

class BaccessResource(resources.ModelResource):

    class Meta:
        model = Baccess
        skip_unchanged = True
        report_skipped = False
        fields = ('name')     
@admin.register(Baccess)
class BaccessAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    resource_class = BaccessResource
    pass

class BusersResource(resources.ModelResource):

    class Meta:
        model = Busers
        skip_unchanged = True
        report_skipped = False
        fields = ("name", "login", "password", "email") 
@admin.register(Busers)
class BusersAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ("name", "login", "email")
    search_fields = ("login__startswith", )
    resource_class = BusersResource
    pass

class bgroupsResource(resources.ModelResource):

    class Meta:
        model = bgroups
        skip_unchanged = True
        report_skipped = False
        fields = ('name')   
@admin.register(bgroups)
class bgroupsAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    resource_class = bgroupsResource
    pass

class ref_userAccessResource(resources.ModelResource):

    class Meta:
        model = ref_userAccess
        skip_unchanged = True
        report_skipped = False
        fields = ("user", "access")   
    
@admin.register(ref_userAccess)
class ref_userAccessAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ("user", "access")
    list_filter = ["access"]
    resource_class = ref_userAccessResource
    actions = [make_general]    
    
class ref_userGroupResource(resources.ModelResource):

    class Meta:
        model = ref_userGroup
        skip_unchanged = True
        report_skipped = False
        fields = ("user", "group")   

@admin.register(ref_userGroup)
class ref_userGroupAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ("user", "group")
    list_filter = ["group"]
    resource_class = ref_userGroupResource
    pass
    
class ref_groupAccessResource(resources.ModelResource):

    class Meta:
        model = ref_groupAccess
        skip_unchanged = True
        report_skipped = False
        fields = ("group", "access")   
    
@admin.register(ref_groupAccess)
class ref_groupAccessAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ("group", "access")
    resource_class = ref_groupAccessResource
    pass

class ref_bookAuthorResource(resources.ModelResource):

    class Meta:
        model = ref_bookAuthor
        skip_unchanged = True
        report_skipped = False
        fields = ("book", "author")   

@admin.register(ref_bookAuthor)
class ref_bookAuthorAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ("book", "author")
    list_filter = ["author"]
    resource_class = ref_bookAuthorResource
    pass

class ref_bookTagsResource(resources.ModelResource):

    class Meta:
        model = ref_bookTags
        skip_unchanged = True
        report_skipped = False
        fields = ("book", "tag")   

@admin.register(ref_bookTags)
class ref_bookTagsAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ("book", "tag")
    list_filter = ["tag"]
    resource_class = ref_bookTagsResource
    pass

    