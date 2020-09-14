from django.contrib import admin
from .models import users, sets, book, SetStatus

# Register your models here.
admin.site.register(users)
admin.site.register(sets)
admin.site.register(book)
admin.site.register(SetStatus)