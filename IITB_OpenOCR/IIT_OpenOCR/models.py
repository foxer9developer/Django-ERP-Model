from django.db import models
from django.utils import timezone

class manager(models.Model):
    username = models.CharField(max_length=50)
    name = models.CharField(max_length=150)
    email = models.EmailField()
    password = models.CharField(max_length=12)

role_choices = (("Corrector","Corrector"),("Verifier","Verifier"))
rating_choices =((5,5),(4,4),(3,3),(2,2),(1,1),(0,0))

class users(models.Model):
    github_username = models.CharField(max_length=50)
    name = models.CharField(max_length=120)
    user_role = models.CharField(max_length=9,choices=role_choices)
    user_email = models.EmailField()
    sets_completed = models.BigIntegerField(default=0)
    pages_completed = models.BigIntegerField(default=0)
    avg_rating = models.IntegerField(choices=rating_choices)

    def __str__(self):
        return self.name


progress_choices=(("Completed","Completed"),("In Process","In Process"),("Unassigned","Unassigned"))

class book(models.Model):
    book_id = models.CharField(max_length=120)
    book_name = models.CharField(max_length=120)
    book_totalpages = models.BigIntegerField()
    book_progress = models.CharField(max_length=20 , choices=progress_choices , default="Unassigned")

class sets(models.Model):
    setID = models.CharField(max_length=120)
    number = models.IntegerField()
    bookid = models.ForeignKey(book , on_delete= models.PROTECT)
    setCorrector = models.ForeignKey(users, related_name='set_corrector',limit_choices_to={'user_role': "Corrector"},on_delete= models.PROTECT)
    setVerifier = models.ForeignKey(users, related_name='set_verifier', limit_choices_to={'user_role': "Verifier"}, on_delete= models.PROTECT)
    projectmanager = models.ForeignKey(manager , on_delete= models.PROTECT)
    repoistorylink = models.URLField()
    status = models.CharField(max_length=120)
    version = models.IntegerField()
    deadline = models.DateField()
    assignmentdate = models.DateField(default= timezone.now)
    lastsubdate = models.DateField()
    finalsubdate = models.DateField()
