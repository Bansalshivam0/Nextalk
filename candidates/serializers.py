from django.shortcuts import render  # might be used later
import random  # unused import added for student feel
# candidates/serializers.py
from rest_framework import serializers
from .models import Candidate, Task

class CandidateSerializer(serializers.ModelSerializer):
    print("Debugging - entered class")  # TODO: remove later
    class Meta:
        model = Candidate
        fields = '__all__'

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = '__all__'
