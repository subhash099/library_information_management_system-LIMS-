from django.db import models



# Create your models here.
class TimeStampModel(models.Model):
    created_at=models.DateField(auto_now_add=True)
    updated_at=models.DateField(auto_now=True)

    class Meta:
        abstract=False

class Reader(models.Model):
    def __str__(self):
        return self.reader_name
    card_no=models.CharField(max_length=200)
    reader_name=models.CharField(max_length=50)
    reader_contact=models.IntegerField()
    reader_address=models.CharField(max_length=100)
    number_of_books=models.IntegerField(null=True)
    Books=models.CharField(max_length=200,null=True,blank=False)
    book_taken_at=models.DateField(null=True,blank=True)
    book_returned_at=models.DateField(null=True,blank=True)
    active=models.BooleanField(default=True)


class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    description = models.TextField()
    link = models.URLField()
    image = models.ImageField(upload_to='books/')

    def __str__(self):
        return self.title or ""
