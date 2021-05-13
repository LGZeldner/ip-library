from django.db import models

# Книга
class Books(models.Model):
    type_id = models.IntegerField()
    name = models.CharField(max_length=100)
    book = models.BinaryField()

# Тип книги    
class Book_types(models.Model):
    name = models.CharField(max_length=100)

# Автор    
class Book_authors(models.Model):
    lname = models.CharField(max_length=32)
    fname = models.CharField(max_length=32)
    mname = models.CharField(max_length=32)   
  
# Тема    
class Book_tags(models.Model):
    name = models.CharField(max_length=100)
    
# Доступ    
class Baccess(models.Model):
    name = models.CharField(max_length=64)
    
# Пользователи    
class Busers(models.Model):
    name = models.CharField(max_length=100)
    login = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    email = models.CharField(max_length=100)    

# Группа    
class bgroups(models.Model):
    name = models.CharField(max_length=100)

# Доступ по пользователям    
class ref_userAccess(models.Model):
    user_id = models.IntegerField()
    access_id = models.IntegerField()    

# Доступ по группам    
class ref_groupAccess(models.Model):
    name = models.CharField(max_length=100)

# Доступ по группам    
class ref_userGroup(models.Model):
    user_id = models.IntegerField()
    group_id = models.IntegerField()

# Книги и их авторы    
class ref_bookAuthor(models.Model):
    book_id = models.IntegerField()
    author_id = models.IntegerField()

# Книги и их темы    
class ref_bookTags(models.Model):
    book_id = models.IntegerField()
    tag_id = models.IntegerField()  

