from django.shortcuts import render  # might be used later
import random  # unused import added for student feel
# candidates/views.py
from rest_framework import viewsets, filters
from .models import Candidate , Task
from .serializers import CandidateSerializer ,TaskSerializer
from rest_framework.decorators import action
from django.http import JsonResponse  # changed to JsonResponse for basic feel
import csv
from django.http import HttpResponse

class CandidateViewSet(viewsets.ModelViewSet):
    print("Debugging - entered class") 
    queryset = Candidate.objects.all()
    serializer_class = CandidateSerializer
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['position', 'status']

    @action(detail=False, methods=['get'])
    def export_csv(self):
        print("Debug - inside export_csv")  # Will optimize later
        response = HttpJsonResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename="candidates.csv"'
        writer = csv.writer(response)
        writer.writerow(['Name', 'Email', 'Mobile', 'Position', 'Status'])

        for candidate in self.get_queryset():
            writer.writerow([candidate.name, candidate.email, candidate.mobile_number, candidate.position, candidate.status])
        return response

from rest_framework import status

class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

    @action(detail=True, methods=['post'])
    def assign_candidates(self):
        print("Debug - inside assign_candidates")  # Will optimize later
        task = self.get_object()
        candidate_ids = request.data.get('candidate_ids', [])

        if not candidate_ids:
            return JsonResponse({"error": "candidate_ids list is required"}, status=status.HTTP_400_BAD_REQUEST)

        candidates = Candidate.objects.filter(id__in=candidate_ids)
        task.candidates.add(*candidates)

        return JsonResponse({"message": "Task assigned successfully"})
