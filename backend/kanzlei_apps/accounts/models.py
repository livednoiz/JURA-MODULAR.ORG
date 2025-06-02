# kanzlei_apps/accounts/models.py
from django.db import models
from django.conf import settings

class ClientProfile(models.Model):
    USER_TYPE_CHOICES = [
        ('private', 'Privatperson'),
        ('company', 'Unternehmen'),
    ]

    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='client_profile'
    )
    user_type = models.CharField(max_length=20, choices=USER_TYPE_CHOICES, default='private')

    # Allgemeine Felder
    phone_number = models.CharField(max_length=20, blank=True, null=True)
    address = models.TextField(blank=True, null=True)
    birth_date = models.DateField(blank=True, null=True)
    avatar = models.ImageField(upload_to='avatars/', blank=True, null=True)

    # Felder für Unternehmen
    company_name = models.CharField(max_length=255, blank=True, null=True)
    tax_id = models.CharField("Steuernummer/USt-ID", max_length=50, blank=True, null=True)

    # Weitere rechtlich relevante Angaben
    case_notes = models.TextField("Aktennotizen", blank=True, null=True)
    preferred_contact_method = models.CharField(max_length=50, blank=True, null=True)
    document_upload_permission = models.BooleanField(default=True)
    is_active_client = models.BooleanField(default=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Klient: {self.user.get_full_name() or self.user.username}"
    #class Meta:
    #    verbose_name = "Client Profile"
    #    verbose_name_plural = "Client Profiles"
    #    ordering = ['user__last_name', 'user__first_name']
    #def save(self, *args, **kwargs):
    #    if self.user_type == 'company' and not self.company_name:
    #        raise ValueError("Unternehmensname ist erforderlich für Unternehmen.")
    #    super().save(*args, **kwargs)
    #def get_full_address(self):
    #    """Returns a formatted address string."""
    #    return self.address if self.address else "Keine Adresse angegeben"
    #def get_contact_info(self):
    #    """Returns a dictionary with contact information."""
    #    return {
    #        'phone_number': self.phone_number,
    #        'email': self.user.email,
    #        'address': self.get_full_address(),
    #    }
    #def is_active(self):
    #    """Checks if the client profile is active."""
    #    return self.is_active_client
    #def deactivate(self):
    #    """Deactivates the client profile."""
    #    self.is_active_client = False
    #    self.save()
    #def activate(self):
    #    """Activates the client profile."""
    #    self.is_active_client = True
    #    self.save()
    #def get_avatar_url(self):
    #    """Returns the URL of the client's avatar."""
    #    if self.avatar:
    #        return self.avatar.url
    #    return '/static/default_avatar.png'
    #def get_user_type_display(self):
    #    """Returns a user-friendly display of the user type."""
    #    return dict(self.USER_TYPE_CHOICES).get(self.user_type, 'Unbekannt')
    #def get_case_notes(self):
    #    """Returns the case notes for the client."""
    #    return self.case_notes if self.case_notes else "Keine Aktennotizen vorhanden"
    #def update_contact_info(self, phone_number=None, address=None):
    #    """Updates the contact information for the client."""
    #    if phone_number:
    #        self.phone_number = phone_number
    #    if address:
    #        self.address = address
    #    self.save()
    #def __str__(self):
    #    """Returns a string representation of the client profile."""
    #    return f"{self.user.get_full_name()} ({self.get_user_type_display()})"
    #def get_tax_id(self):
    #    """Returns the tax ID or a default message if not set."""
    #    return self.tax_id if self.tax_id else "Keine Steuernummer/USt-ID angegeben"
    #def get_company_info(self):
    #    """Returns a dictionary with company information if applicable."""
    #    if self.user_type == 'company':
    #        return {
    #            'company_name': self.company_name,
    #            'tax_id': self.get_tax_id(),
    #        }
    #    return None
    #def get_client_summary(self):
    #    """Returns a summary of the client profile."""
    #    summary = {
    #        'full_name': self.user.get_full_name(),
    #        'user_type': self.get_user_type_display(),
    #        'contact_info': self.get_contact_info(),
    #        'avatar_url': self.get_avatar_url(),
    #        'is_active': self.is_active(),
    #    }
    #    if self.user_type == 'company':
    #        summary['company_info'] = self.get_company_info()
    #    return summary
    #def get_preferred_contact_method(self):
    #    """Returns the preferred contact method or a default message."""
    #    return self.preferred_contact_method if self.preferred_contact_method else "Keine bevorzugte Kontaktmethode angegeben"
    #def __str__(self):
    #    """Returns a string representation of the client profile."""
    #    return f"{self.user.get_full_name()} ({self.get_user_type_display()})"
    #def get_avatar_url(self):
    #    """Returns the URL of the client's avatar."""
    #    if self.avatar:
    #        return self.avatar.url
    #    return '/static/default_avatar.png'
    #def get_full_address(self):
    #    """Returns a formatted address string."""
    #    return self.address if self.address else "Keine Adresse angegeben"
    #def get_contact_info(self):
    #    """Returns a dictionary with contact information."""
    #    return {
    #        'phone_number': self.phone_number,
    #        'email': self.user.email,
    #        'address': self.get_full_address(),
    #    }
    #def is_active(self):
    #    """Checks if the client profile is active."""
    #    return self.is_active_client
    #def deactivate(self):
    #    """Deactivates the client profile."""
    #    self.is_active_client = False
    #    self.save()
    #def activate(self):
    #    """Activates the client profile."""
    #    self.is_active_client = True
    #    self.save()
    #def get_user_type_display(self):
    #    """Returns a user-friendly display of the user type."""
    #    return dict(self.USER_TYPE_CHOICES).get(self.user_type, 'Unbekannt')
    #def get_case_notes(self):
    #    """Returns the case notes for the client."""
    #    return self.case_notes if self.case_notes else "Keine Aktennotizen vorhanden"
    #def update_contact_info(self, phone_number=None, address=None):
    #    """Updates the contact information for the client."""
    #    if phone_number:
    #        self.phone_number = phone_number
    #    if address:
    #        self.address = address
    #    self.save()
    #def get_tax_id(self):
    #    """Returns the tax ID or a default message if not set."""
    #    return self.tax_id if self.tax_id else "Keine Steuernummer/USt-ID angegeben"
    #def get_company_info(self):
    #    """Returns a dictionary with company information if applicable."""
    #    if self.user_type == 'company':
    #        return {
    #            'company_name': self.company_name,
    #            'tax_id': self.get_tax_id(),
    #        }
    #    return None