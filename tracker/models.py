from django.db import models


# Create your models here.
class account(models.Model):
    ADMIN = 'AD'
    LEVEL1 = 'L1'
    LEVEL2 = 'L2'
    LOCKED = 'L3'
    ACCOUNT_PRIORITY_CHOICES = [
        (ADMIN, 'Admin'),
        (LEVEL1, 'Level1'),
        (LEVEL2, 'Level2'),
        (LOCKED, 'Locked'),
    ]
    accountID = models.AutoField(primary_key=True)
    name = models.CharField(max_length=32, blank=True, default="")
    description = models.TextField(max_length=256, blank=True, default="")
    email = models.EmailField(max_length=254)
    dateCreated = models.DateTimeField(auto_now_add=True)
    dateModified = models.DateTimeField(auto_now=True)
    priority = models.CharField(
        max_length=2,
        choices=ACCOUNT_PRIORITY_CHOICES,
        default=LEVEL1,
    )

    def is_admin(self):
        return self.priority in self.ADMIN

    def is_locked(self):
        return self.priority in self.LOCKED

    def __str__(self):
        return self.name


class record(models.Model):
    INIT = 'IN'
    OPEN = 'OP'
    BLOCKED = 'BL'
    RESOLVED = 'RE'
    CLOSED = 'CL'
    RECORD_STATUS_CHOICES = [
        (INIT, 'Initial'),
        (OPEN, 'Opened'),
        (BLOCKED, 'Blocked'),
        (RESOLVED, 'Resolved'),
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
    title = models.CharField(max_length=32, blank=True, default="")
    description = models.TextField(max_length=256, blank=True, default="")
    originator = models.ForeignKey('account', related_name='originator', on_delete=models.DO_NOTHING)
    assigned = models.ForeignKey('account', related_name='assigned', on_delete=models.DO_NOTHING)
    dateCreated = models.DateTimeField(auto_now_add=True)
    dateModified = models.DateTimeField(auto_now=True)
    comments = models.ForeignKey('recordComment', on_delete=models.CASCADE, blank=True, null=True)
    resolution = models.TextField(max_length=256, blank=True, default="")

    def is_opened(self):
        return self.status in self.OPEN

    def is_closed(self):
        return self.status in self.CLOSED

    def is_blocked(self):
        return self.status in self.BLOCKED

    def __str__(self):
        return self.title


class project(models.Model):
    projectID = models.AutoField(primary_key=True)
    name = models.CharField(max_length=32, blank=True, default="")
    description = models.TextField(max_length=256, blank=True, default="")
    owner = models.ForeignKey('account', on_delete=models.DO_NOTHING)
    dateCreated = models.DateTimeField(auto_now_add=True)
    dateModified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class recordComment(models.Model):
    commentID = models.AutoField(primary_key=True)
    title = models.CharField(max_length=32, blank=True, default="")
    content = models.TextField(max_length=256, blank=True, default="")
    owner = models.ForeignKey('account', on_delete=models.DO_NOTHING)
    dateCreated = models.DateTimeField(auto_now_add=True)
    dateModified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
