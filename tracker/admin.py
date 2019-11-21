from django.contrib import admin

# Register your models here.
from .models import (
    record,
    project,
    recordComment
)

admin.site.register(record)
admin.site.register(project)
admin.site.register(recordComment)

