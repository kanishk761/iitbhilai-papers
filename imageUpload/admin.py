from django.contrib import admin
from .models import paperModel
from .models import courseModel

# Register your models here.
admin.site.register(paperModel)
admin.site.register(courseModel)
