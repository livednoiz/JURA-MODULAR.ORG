#from django.shortcuts import render

# Create your views here.
# cases/views.py
from rest_framework import viewsets
from .models import Case
from .serializers import CaseSerializer
from .permissions import CanViewOrAssignCases

class CaseViewSet(viewsets.ModelViewSet):
    serializer_class = CaseSerializer
    permission_classes = [CanViewOrAssignCases]

    def get_queryset(self):
        user = self.request.user

        # Alle Fälle, wenn der Benutzer das darf
        if user.has_perm('kanzlei_apps.view_all_cases'):
            return Case.objects.all()
        
        # Andernfalls nur zugewiesene Fälle
        return Case.objects.filter(assigned_to=user)
