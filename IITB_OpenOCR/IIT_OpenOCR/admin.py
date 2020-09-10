from django.contrib import admin
from .models import manager
from .models import users
from .models import sets
from .models import book

# Register your models here.
admin.site.register(manager)
admin.site.register(users)
admin.site.register(sets)
admin.site.register(book)