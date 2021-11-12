from django.db import models

# Книга
class Books(models.Model):
    type = models.ForeignKey('Book_types', on_delete=models.SET_NULL, null=True)
    name = models.CharField(max_length=100)
    book = models.CharField(max_length=65535)
    def __str__(self):
        return f"{self.type, self.name, self.book}"
    class Meta:
        ordering = ["name"]

# Тип книги    
class Book_types(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return f"{self.name}"

# Автор    
class Book_authors(models.Model):
    lname = models.CharField(max_length=32)
    fname = models.CharField(max_length=32)
    mname = models.CharField(max_length=32)  
    def __str__(self):
        return f"{self.fname, self.mname, self.lname}"
  
# Теги    
class Book_tags(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return f"{self.name}"
    
# Доступ    
class Baccess(models.Model):
    name = models.CharField(max_length=64)
    def __str__(self):
        return f"{self.name}"
    
# Пользователи    
class Busers(models.Model):
    name = models.CharField(max_length=100)
    login = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    def __str__(self):
        return f"{self.name, self.login, self.email}"    

# Группа    
class bgroups(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return f"{self.name}"

# Доступ по пользователям    
class ref_userAccess(models.Model):
    user = models.ForeignKey('Busers', on_delete=models.SET_NULL, null=True)
    access = models.ForeignKey('Baccess', on_delete=models.SET_NULL, null=True)
    def __str__(self):
        return f"{self.user, self.access}"    

# Доступ по группам    
class ref_groupAccess(models.Model):
    group = models.ForeignKey('bgroups', on_delete=models.SET_NULL, null=True)
    access = models.ForeignKey('Baccess', on_delete=models.SET_NULL, null=True)
    def __str__(self):
        return f"{self.group, self.access}"    

# Доступ по группам    
class ref_userGroup(models.Model):
    user = models.ForeignKey('Busers', on_delete=models.SET_NULL, null=True)
    group = models.ForeignKey('bgroups', on_delete=models.SET_NULL, null=True)
    def __str__(self):
        return f"{self.user, self.group}"

# Книги и их авторы    
class ref_bookAuthor(models.Model):
    book = models.ForeignKey('Books', on_delete=models.SET_NULL, null=True)
    author = models.ForeignKey('Book_authors', on_delete=models.SET_NULL, null=True)
    def __str__(self):
        return f"{self.book, self.author}"

# Книги и их темы    
class ref_bookTags(models.Model):
    book = models.ForeignKey('Books', on_delete=models.SET_NULL, null=True)
    tag = models.ForeignKey('Book_tags', on_delete=models.SET_NULL, null=True)
    def __str__(self):
        return f"{self.book, self.tag}"    

