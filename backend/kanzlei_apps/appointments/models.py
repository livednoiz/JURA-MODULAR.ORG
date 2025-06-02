# kanzlei_apps/appointments/models.py
from django.db import models
from django.conf import settings
from datetime import datetime
from django.utils import timezone

class AppointmentRequest(models.Model):
    client = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='appointment_requests'
    )
    preferred_date = models.DateField()
    preferred_time = models.TimeField()
    note = models.TextField(blank=True, null=True)
    is_confirmed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Terminwunsch von {self.client.username} für {self.preferred_date}"
    class Meta:
        verbose_name = "Terminwunsch"
        verbose_name_plural = "Terminwünsche"
        ordering = ['-created_at']
    def get_client_name(self):
        """Returns the full name of the client."""
        return self.client.get_full_name() if self.client else "Unbekannt"
    def get_preferred_datetime(self):
        """Returns the preferred date and time as a datetime object."""
        return datetime.combine(self.preferred_date, self.preferred_time) if self.preferred_date and self.preferred_time else None
    def is_upcoming(self):
        """Checks if the appointment request is for a future date."""
        return self.preferred_date > timezone.now().date() or (
            self.preferred_date == timezone.now().date() and self.preferred_time > timezone.now().time()
        )
    def confirm(self):
        """Marks the appointment request as confirmed."""
        self.is_confirmed = True
        self.save()
    def cancel(self):
        """Cancels the appointment request."""
        self.is_confirmed = False
        self.save()
    def get_note(self):
        """Returns the note associated with the appointment request."""
        return self.note if self.note else "Keine Notiz vorhanden"
    def get_created_at(self):
        """Returns the date and time when the appointment request was created."""
        return self.created_at.strftime('%Y-%m-%d %H:%M:%S') if self.created_at else "Unbekannt"
    def delete(self, *args, **kwargs):
        """Deletes the appointment request."""
        super().delete(*args, **kwargs)
        # Additional cleanup can be added here if needed
    def save(self, *args, **kwargs):
        """Custom save method to ensure preferred date and time are valid."""
        if not self.preferred_date or not self.preferred_time:
            raise ValueError("Bevorzugtes Datum und Uhrzeit müssen angegeben werden.")
        super().save(*args, **kwargs)
        # Additional logic can be added here if needed
    def get_status(self):
        """Returns the status of the appointment request."""
        return "Bestätigt" if self.is_confirmed else "Ausstehend"
    def get_client_contact_info(self):
        """Returns a dictionary with the client's contact information."""
        return {
            'username': self.client.username,
            'email': self.client.email,
            'full_name': self.get_client_name(),
        }
    def get_appointment_details(self):
        """Returns a dictionary with the appointment request details."""
        return {
            'client': self.get_client_contact_info(),
            'preferred_date': self.preferred_date,
            'preferred_time': self.preferred_time,
            'note': self.get_note(),
            'is_confirmed': self.is_confirmed,
            'created_at': self.get_created_at(),
        }
    def get_absolute_url(self):
        """Returns the absolute URL for the appointment request."""
        return f"/appointments/requests/{self.id}/"
    def get_client_url(self):
        """Returns the URL for the client's profile."""
        return f"/users/{self.client.id}/profile/"
    def get_preferred_datetime_str(self):
        """Returns the preferred date and time as a formatted string."""
        return f"{self.preferred_date} {self.preferred_time.strftime('%H:%M')}" if self.preferred_date and self.preferred_time else "Unbekannt"
    def get_appointment_summary(self):
        """Returns a summary of the appointment request."""
        return f"{self.get_client_name()} - {self.get_preferred_datetime_str()} ({self.get_status()})"
    def get_appointment_request_info(self):
        """Returns a dictionary with detailed information about the appointment request."""
        return {
            'id': self.id,
            'client': self.get_client_contact_info(),
            'preferred_datetime': self.get_preferred_datetime_str(),
            'note': self.get_note(),
            'is_confirmed': self.is_confirmed,
            'created_at': self.get_created_at(),
            'status': self.get_status(),
        }
    def __str__(self):
        """Returns a string representation of the appointment request."""
        return f"Terminwunsch von {self.get_client_name()} am {self.preferred_date} um {self.preferred_time.strftime('%H:%M')}"
    def get_client_avatar_url(self):
        """Returns the URL of the client's avatar."""
        return self.client.profile.get_avatar_url() if hasattr(self.client, 'profile') else '/static/default_avatar.png'
    def get_client_full_address(self):
        """Returns the full address of the client."""
        return self.client.profile.get_full_address() if hasattr(self.client, 'profile') else "Keine Adresse angegeben"
    def get_client_phone_number(self):
        """Returns the phone number of the client."""
        return self.client.profile.phone_number if hasattr(self.client, 'profile') else "Keine Telefonnummer angegeben"
    def get_client_email(self):
        """Returns the email address of the client."""
        return self.client.email if self.client else "Keine E-Mail-Adresse angegeben"
    def get_client_type(self):
        """Returns the type of the client (e.g., individual, company)."""
        return self.client.profile.user_type if hasattr(self.client, 'profile') else "Unbekannt"
    def get_client_tax_id(self):
        """Returns the tax ID of the client if applicable."""
        return self.client.profile.tax_id if hasattr(self.client, 'profile') and self.client.profile.user_type == 'company' else "Keine Steuernummer/USt-ID angegeben"
    def get_client_company_info(self):
        """Returns a dictionary with company information if the client is a company."""
        if hasattr(self.client, 'profile') and self.client.profile.user_type == 'company':
            return {
                'company_name': self.client.profile.company_name,
                'tax_id': self.get_client_tax_id(),
            }
        return None
    def get_client_summary(self):
        """Returns a summary of the client's profile."""
        summary = {
            'full_name': self.get_client_name(),
            'user_type': self.get_client_type(),
            'contact_info': {
                'phone_number': self.get_client_phone_number(),
                'email': self.get_client_email(),
                'address': self.get_client_full_address(),
            },
            'avatar_url': self.get_client_avatar_url(),
            'is_active': self.client.is_active,
        }
        if self.get_client_company_info():
            summary['company_info'] = self.get_client_company_info()
        return summary
    def get_preferred_contact_method(self):
        """Returns the preferred contact method of the client."""
        return self.client.profile.preferred_contact_method if hasattr(self.client, 'profile') else "Keine bevorzugte Kontaktmethode angegeben"
    def get_appointment_request_summary(self):
        """Returns a summary of the appointment request."""
        return {
            'client': self.get_client_summary(),
            'preferred_datetime': self.get_preferred_datetime_str(),
            'note': self.get_note(),
            'status': self.get_status(),
            'created_at': self.get_created_at(),
        }
    def get_appointment_request_details(self):
        """Returns detailed information about the appointment request."""
        return {
            'id': self.id,
            'client': self.get_client_summary(),
            'preferred_datetime': self.get_preferred_datetime_str(),
            'note': self.get_note(),
            'is_confirmed': self.is_confirmed,
            'created_at': self.get_created_at(),
            'status': self.get_status(),
            'contact_method': self.get_preferred_contact_method(),
        }
    def get_appointment_request_metadata(self):
        """Returns metadata about the appointment request."""
        return {
            'id': self.id,
            'client': self.get_client_summary(),
            'preferred_datetime': self.get_preferred_datetime_str(),
            'note': self.get_note(),
            'is_confirmed': self.is_confirmed,
            'created_at': self.get_created_at(),
            'status': self.get_status(),
            'contact_method': self.get_preferred_contact_method(),
            'avatar_url': self.get_client_avatar_url(),
            'full_address': self.get_client_full_address(),
            'phone_number': self.get_client_phone_number(),
        }
    def get_appointment_request_info(self):
        """Returns a dictionary with detailed information about the appointment request."""
        return {
            'id': self.id,
            'client': self.get_client_summary(),
            'preferred_datetime': self.get_preferred_datetime_str(),
            'note': self.get_note(),
            'is_confirmed': self.is_confirmed,
            'created_at': self.get_created_at(),
            'status': self.get_status(),
            'contact_method': self.get_preferred_contact_method(),
            'avatar_url': self.get_client_avatar_url(),
            'full_address': self.get_client_full_address(),
            'phone_number': self.get_client_phone_number(),
        }
    def get_appointment_request_summary(self):
        """Returns a summary of the appointment request."""
        return {
            'id': self.id,
            'client': self.get_client_summary(),
            'preferred_datetime': self.get_preferred_datetime_str(),
            'note': self.get_note(),
            'status': self.get_status(),
            'created_at': self.get_created_at(),
            'contact_method': self.get_preferred_contact_method(),
        }
    def get_appointment_request_url(self):
        """Returns the URL for the appointment request."""
        return f"/appointments/requests/{self.id}/"
    def get_client_profile_url(self):
        """Returns the URL for the client's profile."""
        return f"/users/{self.client.id}/profile/"