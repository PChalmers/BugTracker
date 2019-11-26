from django.db import models


# Create your models here.
class user(models.Model):
    ADMIN = 'AD'
    LEVEL1 = 'L1'
    LEVEL2 = 'L2'
    LEVEL3 = 'L3'
    USER_PRIORITY_CHOICES = [
        (ADMIN, 'Admin'),
        (LEVEL1, 'Opened'),
        (LEVEL2, 'Blocked'),
        (LEVEL3, 'Closed'),
    ]
    userID = models.AutoField(primary_key=True)
    name = models.CharField(max_length=32, blank=True, null=True)
    description = models.CharField(max_length=256, blank=True, null=True)
    email = models.EmailField(max_length=254)
    dateCreated = models.DateTimeField(auto_now_add=True)
    dateModified = models.DateTimeField(auto_now=True)
    priority = models.CharField(
        max_length=2,
        choices=USER_PRIORITY_CHOICES,
        default=LEVEL1,
    )


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
    recordID = models.AutoField(primary_key=True)
    projectId = models.ForeignKey('project', on_delete=models.CASCADE)
    title = models.CharField(max_length=32, blank=True, null=True)
    description = models.CharField(max_length=256, blank=True, null=True)
    ownerEmail = models.EmailField(max_length=254)
    dateCreated = models.DateTimeField(auto_now_add=True)
    dateModified = models.DateTimeField(auto_now=True)
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
    projectID = models.AutoField(primary_key=True)
    name = models.CharField(max_length=32, blank=True, null=True)
    description = models.CharField(max_length=256, blank=True, null=True)
    ownerEmail = models.EmailField(max_length=254)

    def __str__(self):
        return self.name


class recordComment(models.Model):
    commentID = models.AutoField(primary_key=True)
    title = models.CharField(max_length=32, blank=True, null=True)
    content = models.CharField(max_length=256, blank=True, null=True)
    ownerEmail = models.EmailField(max_length=254)
    dateCreated = models.DateTimeField(auto_now_add=True)
    dateModified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
