from django.db import models
from django.utils import timezone

role_choices = (("Corrector","Corrector"),("Verifier","Verifier"),("Project Manager", "Project Manager"))
rating_choices =((5,5),(4,4),(3,3),(2,2),(1,1),(0,0))

class SetStatus(models.Model):
    github_username = models.ForeignKey('users' , on_delete= models.PROTECT, null=True)
    sets_completed = models.BigIntegerField(default=0)
    pages_completed = models.BigIntegerField(default=0)
    avg_rating = models.IntegerField(choices=rating_choices, default=0)

class users(models.Model):
    github_username = models.CharField(max_length=50, unique=True)
    name = models.CharField(max_length=120)
    user_role = models.CharField(max_length=15,choices=role_choices, default='Corrector')
    user_email = models.EmailField()
    user_sets = models.ForeignKey(SetStatus , on_delete= models.PROTECT, null=True,)

    USERNAME_FIELD = 'github_username'
    REQUIRED_FIELDS = ['github_username', 'name','user_email','user_role']

    def __str__(self):
        return self.name


progress_choices=(("Completed","Completed"),("In Process","In Process"),("Unassigned","Unassigned"))

class book(models.Model):
    book_id = models.CharField(max_length=120, unique=True)
    book_name = models.CharField(max_length=120)
    book_totalpages = models.BigIntegerField()
    book_totalsets = models.IntegerField(default=0)
    book_setCompleted = models.IntegerField(default=0)

    def __str__(self):
        return self.book_id

class sets(models.Model):
    setID = models.CharField(max_length=120, unique=True)
    number = models.IntegerField()
    bookid = models.ForeignKey(book , on_delete= models.PROTECT)
    setCorrector = models.ForeignKey(users, related_name='set_corrector',limit_choices_to={'user_role': "Corrector"},on_delete= models.PROTECT)
    setVerifier = models.ForeignKey(users, related_name='set_verifier', limit_choices_to={'user_role': "Verifier"}, on_delete= models.PROTECT)
    projectmanager = models.ForeignKey(users ,related_name='set_projectmanager', limit_choices_to={'user_role': "Project Manager"},  on_delete= models.PROTECT)
    repoistorylink = models.URLField()
    status = models.CharField(max_length=120)
    version = models.IntegerField()
    deadline = models.DateField()
    assignmentdate = models.DateField(default= timezone.now)
    lastsubdate = models.DateField()
    finalsubdate = models.DateField()

    def __str__(self):
        return self.setID

class log(models.Model):
    logID= models.CharField(max_length=50, unique=True)
    log_setID= models.ForeignKey(sets, on_delete=models.PROTECT)

    def __str__(self):
        return self.logID