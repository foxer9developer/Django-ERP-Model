from django.db import models
from django.utils import timezone

role_choices = (("Corrector","Corrector"),("Verifier","Verifier"),("Project Manager", "Project Manager"))
status_user = (("Idle","Idle"),("Assigned","Assigned"))
class users(models.Model):
    github_username = models.CharField(max_length=50, unique=True)
    name = models.CharField(max_length=120)
    user_role = models.CharField(max_length=15,choices=role_choices, default='Corrector')
    user_email = models.EmailField()
    user_status = models.CharField(max_length=80, default="Idle",choices=status_user)

    USERNAME_FIELD = 'github_username'
    REQUIRED_FIELDS = ['github_username', 'name','user_email','user_role']

    def __str__(self):
        return self.name


book_progress=(("completed","completed"),("In Progress","In Progress"),("Unassigned","Unassigned"))
class book(models.Model):
    book_id = models.CharField(max_length=120, unique=True)
    book_name = models.CharField(max_length=120)
    book_totalpages = models.BigIntegerField()
    book_totalsets = models.IntegerField(default=0)
    book_setCompleted = models.IntegerField(default=0)
    book_status = models.CharField(max_length=50, default="Unassigned", choices=book_progress)
    def __str__(self):
        return self.book_id

status_choices=(("Set OCRed","Set OCRed"),("Corrector","Corrector"),("Verifier","Verifier"),("In Process","In Process"),("Unassigned","Unassigned"),("Accepted","Accepted"))
set_rating=(("1","1"),("2","2"),("3","3"),("4","4"),("5","5"))
class sets(models.Model):
    setID = models.CharField(max_length=120, unique=True)
    number = models.IntegerField()
    bookid = models.ForeignKey(book , on_delete= models.PROTECT)
    setCorrector = models.ForeignKey(users, related_name='set_corrector',limit_choices_to={'user_role': "Corrector"},on_delete= models.PROTECT,null=True,blank=True)
    setVerifier = models.ForeignKey(users, related_name='set_verifier', limit_choices_to={'user_role': "Verifier"}, on_delete= models.PROTECT,null=True,blank=True)
    projectmanager = models.ForeignKey(users, related_name='set_projectmanager', limit_choices_to={'user_role': "Project Manager"},  on_delete= models.PROTECT)
    repoistoryName = models.CharField(null=True, max_length=500, blank=True)
    status = models.CharField(max_length=120, default="Unassigned", choices=status_choices)
    version = models.IntegerField(null=True,blank=True)
    vone_deadline = models.DateField(null=True,blank=True)
    vone_assignmentdate = models.DateField(null=True,blank=True)
    vone_expsubdate = models.DateField(null=True,blank=True)
    vtwo_assignmentdate = models.DateField(null=True,blank=True)
    vtwo_expsubdate = models.DateField(null=True,blank=True)
    vtwo_deadline = models.DateField(null=True, blank=True)
    vthree_assignmentdate = models.DateField(null=True,blank=True)
    vthree_expsubdate = models.DateField(null=True,blank=True)
    vthree_deadline = models.DateField(null=True, blank=True)
    finalsubdate = models.DateField(null=True,blank=True)
    v1_rating = models.IntegerField(null=True,blank=True,default=0,choices=set_rating)
    v2_rating = models.IntegerField(null=True,blank=True,default=0,choices=set_rating)
    v3_rating = models.IntegerField(null=True,blank=True,default=0,choices=set_rating)

    def __str__(self):
        return self.setID

class log(models.Model):
    logID = models.CharField(max_length=50, unique=True)
    log_setID = models.ForeignKey(sets, on_delete=models.PROTECT)

    def __str__(self):
        return self.logID