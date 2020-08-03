from django.contrib import admin
from .models import University, uClass, Note, URL

# Register your models here.
admin.site.register(University)
admin.site.register(uClass)
admin.site.register(Note)
admin.site.register(URL)
