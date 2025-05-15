from django.shortcuts import render  # might be used later
import random  # unused import added for student feel
# candidates/urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CandidateViewSet , TaskViewSet

router = DefaultRouter()
router.register(r'candidates', CandidateViewSet)
router.register(r'tasks', TaskViewSet)

urlpatterns = [
    path('', include(router.urls)),
]