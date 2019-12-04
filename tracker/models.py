from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class account(models.Model):
    ACTIVE = 'AC'
    LOCKED = 'LK'
    ACCOUNT_STATUS_CHOICES = [
        (ACTIVE, 'Active'),
        (LOCKED, 'Locked'),
    ]
    accountID = models.AutoField(primary_key=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=64)
    description = models.TextField(max_length=256)
    email = models.EmailField(max_length=254)
    status = models.CharField(
        max_length=2,
        choices=ACCOUNT_STATUS_CHOICES,
        default=ACTIVE,
    )
    dateCreated = models.DateTimeField(auto_now_add=True)
    dateModified = models.DateTimeField(auto_now=True)

    def is_admin(self):
        return self.user.is_staff

    def is_locked(self):
        return self.status in self.LOCKED

    def get_email(self):
        return self.user.email

    def __str__(self):
        return self.name


class record(models.Model):
    INIT = 'IN'
    OPEN = 'OP'
    ASSIGNED = 'AS'
    BLOCKED = 'BL'
    CLOSED = 'CL'
    RECORD_STATUS_CHOICES = [
        (INIT, 'Initial'),
        (OPEN, 'Opened'),
        (ASSIGNED, 'Assigned'),
        (BLOCKED, 'Blocked'),
        (CLOSED, 'Closed'),
    ]
    REQ = 'RE'
    DEFECT = 'DE'
    BUILD = 'BD'
    WORK = 'WK'
    RECORD_TYPE_CHOICES = [
        (REQ, 'Requirement'),
        (DEFECT, 'Defect'),
        (BUILD, 'Build'),
        (WORK, 'Work'),
    ]
    recordID = models.AutoField(primary_key=True)
    projectId = models.ForeignKey('project', on_delete=models.DO_NOTHING)
    type = models.CharField(
        max_length=2,
        choices=RECORD_TYPE_CHOICES,
        default=WORK,
    )
    status = models.CharField(
        max_length=2,
        choices=RECORD_STATUS_CHOICES,
        default=INIT,
    )
    title = models.CharField(max_length=32)
    description = models.TextField(max_length=256)
    originator = models.ForeignKey('account', related_name='originator', on_delete=models.DO_NOTHING)
    assigned = models.ForeignKey('account', related_name='assigned', blank=True, null=True, on_delete=models.DO_NOTHING)
    dateCreated = models.DateTimeField(auto_now_add=True)
    dateModified = models.DateTimeField(auto_now=True)
    comments = models.ForeignKey('recordComment', blank=True, null=True, on_delete=models.CASCADE)

    def is_opened(self):
        return self.status in self.OPEN

    def is_assigned(self):
        return self.status in self.ASSIGNED

    def is_closed(self):
        return self.status in self.CLOSED

    def is_blocked(self):
        return self.status in self.BLOCKED

    def __str__(self):
        return self.title


class project(models.Model):
    projectID = models.AutoField(primary_key=True)
    name = models.CharField(max_length=64)
    description = models.TextField(max_length=256)
    owner = models.ForeignKey('account', on_delete=models.DO_NOTHING)
    dateCreated = models.DateTimeField(auto_now_add=True)
    dateModified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class recordComment(models.Model):
    commentID = models.AutoField(primary_key=True)
    recordID = models.ForeignKey('record', on_delete=models.DO_NOTHING)
    title = models.CharField(max_length=32)
    content = models.TextField(max_length=256)
    owner = models.ForeignKey('account', on_delete=models.DO_NOTHING)
    dateCreated = models.DateTimeField(auto_now_add=True)
    dateModified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
