# users/signals.py
from django.contrib.auth.models import Group, Permission
from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import User

@receiver(post_save, sender=User)
def assign_user_group(sender, instance, created, **kwargs):
    if created and instance.role:
        # Hole oder erstelle die Gruppe
        group, created_group = Group.objects.get_or_create(name=instance.role)

        # Weisen wir der Gruppe ggf. Standard-Permissions zu (einmalig beim Anlegen)
        if created_group:
            if instance.role == 'anwalt':
                permission = Permission.objects.get(codename='view_all_cases')
                group.permissions.add(permission)
            if instance.role == 'sekretariat':
                permission = Permission.objects.get(codename='assign_cases')
                group.permissions.add(permission)

        # Füge den User der Gruppe hinzu
        instance.groups.add(group)
# from django.apps import AppConfig
# class UsersConfig(AppConfig):
#     name = 'users'
#     def ready(self):
#         import users.signals
#         self.register_signals()
# This signal listens for the creation of a User instance and assigns the user to a group based on their role.
# The role is expected to be a string that matches the name of a group.
# Ensure that the groups exist in your database before using this signal.
# If the group does not exist, it will be created automatically.
# This is useful for managing permissions and access control based on user roles.
# Make sure to import this signal in your app's ready method or in the app's __init__.py file
# to ensure it is registered when the app is loaded.
# For example, in your app's apps.py:
# from django.apps import AppConfig