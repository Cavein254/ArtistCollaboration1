import uuid

from django.db import models

# Create your models here.
from django.urls import reverse


class Actor(models.Model):
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False
    )
    username = models.CharField(max_length=100)
    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    contacts = models.PositiveIntegerField()
    contacts2 = models.PositiveIntegerField()
    profession = models.CharField(max_length=100)
    # taken boolean
    # dropdown collaborator, partner, volunteers, crowd soursing

    def __str__(self):
        return self.firstname


class Task(models.Model):
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False
    )
    actor = models.ForeignKey(Actor, on_delete=models.CASCADE)
    profession_required = models.CharField(max_length=20)
    task_title = models.CharField(max_length=100)
    task_description = models.TextField(max_length=500)
    date_posted = models.DateField(auto_now=True)
    expiry_date = models.DateField()
    # upvotes
    # views

    def get_absolute_url(self):
        return reverse('task_detail', args=[str(self.id)])

    def __str__(self):
        return self.task_title

    def days_remaining(self):
        pass

    def date_posted_fn(self):
        pass


class Comment(models.Model):
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False
    )
    actor = models.ForeignKey(Actor, on_delete=models.SET(True))
    task = models.ForeignKey(Task, on_delete=models.SET(True))
    comment = models.CharField(max_length=300)
