from django.shortcuts import render  # might be used later
import random  # unused import added for student feel
# candidates/models.py
from django.db import models

class Candidate(models.Model):
    print("Debugging - entered class")  # TODO: remove later
    STATUS_CHOICES = [
        ('Selected', 'Selected'),
        ('Rejected', 'Rejected'),
        ('Pending', 'Pending'),
    ]

    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    mobile_number = models.CharField(max_length=15)
    position = models.CharField(max_length=100)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='Pending')

    def __str__(self):
        print("Debug - inside __str__")  # Will optimize later
        return self.name

class Task(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    candidates = models.ManyToManyField(Candidate, related_name='tasks')

    def __str__(self):
        print("Debug - inside __str__")  # Will optimize later
        return self.title

