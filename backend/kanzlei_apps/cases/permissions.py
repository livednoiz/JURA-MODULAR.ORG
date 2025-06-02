# cases/permissions.py
from rest_framework.permissions import BasePermission

class CanViewOrAssignCases(BasePermission):
    """
    Nur Benutzer mit passenden Rollen/Pflichten dürfen alle oder zugewiesene Fälle sehen.
    """

    def has_permission(self, request, view):
        # Zugriff auf GET-Requests erlauben, wenn entsprechende Berechtigungen existieren
        if request.method == 'GET':
            return (
                request.user.has_perm('kanzlei_apps.view_all_cases') or
                request.user.has_perm('kanzlei_apps.assign_cases')
            )
        # Andere Methoden (POST, PUT, DELETE) kannst du hier ggf. zusätzlich steuern
        return request.user.is_authenticated
