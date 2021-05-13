from django.db import models

# Книга
class Books(models.Model):
    type_id = models.IntegerField()
    name = models.CharField(max_length=100)
    book = models.BinaryField()
    def __str__(self):
        return f"{self.type_id, self.name, self.book}"
    class Meta:
        ordering = ("name")

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
  
# Тема    
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
    user_id = models.IntegerField()
    access_id = models.IntegerField()
    def __str__(self):
        return f"{self.user_id, self.access_id}"    

# Доступ по группам    
class ref_groupAccess(models.Model):
    group_id = models.IntegerField()
    access_id = models.IntegerField()
    def __str__(self):
        return f"{self.group_id, self.access_id}"    

# Доступ по группам    
class ref_userGroup(models.Model):
    user_id = models.IntegerField()
    group_id = models.IntegerField()
    def __str__(self):
        return f"{self.user_id, self.group_id}"

# Книги и их авторы    
class ref_bookAuthor(models.Model):
    book_id = models.IntegerField()
    author_id = models.IntegerField()
    def __str__(self):
        return f"{self.book_id, self.author_id}"

# Книги и их темы    
class ref_bookTags(models.Model):
    book_id = models.IntegerField()
    tag_id = models.IntegerField()
    def __str__(self):
        return f"{self.book_id, self.tag_id}"    

