from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    genre = models.CharField(max_length=100)
    year_published = models.IntegerField()
    summary = models.TextField()

    def __str__(self):
        return self.title

class Review(models.Model):
    book = models.ForeignKey(Book, related_name='reviews', on_delete=models.CASCADE)
    user_id = models.IntegerField()
    review_text = models.TextField()
    rating = models.IntegerField()

    def __str__(self):
        return f'Review for {self.book.title} by User {self.user_id}'
