# apps/users/apps.py
from django.apps import AppConfig

class UsersConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'kanzlei_apps.users'
    verbose_name = 'Users Management'
    label = 'users'
    def ready(self):
        # Import signals or other startup code here if needed
        import kanzlei_apps.users.signals
        pass
#