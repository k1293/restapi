from django.db import models
from django.utils import timezone

class List(models.Model):
    STATUS_CHOICES = (
        ('done','done'),
        ('undone','undone'),
        ('delete','delete')
    )
    task = models.CharField(max_length=250)
    created = models.DateTimeField(default=timezone.now)
    status = models.CharField(max_length=10, 
                              choices=STATUS_CHOICES, 
                              default='undone') 

class Meta:
    ordering = ('-created')

def __str__(self):
    return self.task

