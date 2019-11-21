from django.db import models


# Create your models here.
class record(models.Model):
    INIT = 'IN'
    OPEN = 'OP'
    BLOCKED = 'BL'
    CLOSED = 'CL'
    RECORD_STATUS_CHOICES = [
        (INIT, 'Initial'),
        (OPEN, 'Opened'),
        (BLOCKED, 'Blocked'),
        (CLOSED, 'Closed'),
    ]
    ID = models.AutoField(primary_key=True),
    projectId = models.ForeignKey('project', on_delete=models.CASCADE),
    title = models.TextField(max_length=32),
    description = models.TextField(max_length=256),
    owner = models.EmailField(max_length=254),
    dateCreated = models.DateTimeField(),
    dateModified = models.DateTimeField(),
    comments = models.ForeignKey('recordComment', on_delete=models.CASCADE)
    status = models.CharField(
        max_length=2,
        choices=RECORD_STATUS_CHOICES,
        default=INIT,
    )

    def is_opened(self):
        return self.status in self.OPEN

    def is_closed(self):
        return self.status in self.CLOSED

    def is_blocked(self):
        return self.status in self.BLOCKED

    def __str__(self):
        return self.title


class project(models.Model):
    ID = models.AutoField(primary_key=True),
    name = models.TextField(max_length=32),
    owner = models.EmailField(max_length=254)

    def __str__(self):
        return self.name


class recordComment(models.Model):
    ID = models.AutoField(primary_key=True),
    title = models.TextField(max_length=32),
    content = models.TextField(max_length=256),
    owner = models.EmailField(max_length=254),
    dateCreated = models.DateTimeField(),
    dateModified = models.DateTimeField()

    def __str__(self):
        return self.title
