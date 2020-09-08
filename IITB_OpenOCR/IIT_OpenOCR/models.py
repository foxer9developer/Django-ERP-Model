from django.db import models

class users(models.Model):
    git_username = models.CharField()
    user_name = models.CharField()
    user_role = models.CharField(max_length=9, help_text=""" Only Corrector or Verifier Allowed  """)
    user_email = models.EmailField()

class book(models.Model):
    book_id = models.CharField()
    book_name = models.CharField()
    book_pages = models.BigIntegerField()


class sets(models.Model):
    sets_bookid = models.ForeignKey(book.book_id, on_delete=models.CASCADE)
    sets_repolink = models.URLField()
    sets_status = models.CharField()
    sets_stage = models.CharField()
    sets_deadlineDate = models.DateTimeField()
    sets_submitDate = models.DateTimeField()








# Create your models here.
