from django.contrib import admin

# Register your models here.
from .models import (
    account,
    record,
    project,
    recordComment
)

admin.site.register(account)
admin.site.register(record)
admin.site.register(project)
admin.site.register(recordComment)

