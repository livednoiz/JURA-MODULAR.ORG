# kanzlei_apps/cases/models.py
from django.db import models
from django.conf import settings

class CaseFile(models.Model):
    STATUS_CHOICES = [
        ('open', 'Offen'),
        ('in_progress', 'In Bearbeitung'),
        ('closed', 'Abgeschlossen'),
    ]

    client = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='cases'
    )
    title = models.CharField(max_length=255)
    description = models.TextField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='open')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Fall: {self.title} ({self.get_status_display()})"
class CaseDocument(models.Model):
    case = models.ForeignKey(CaseFile, on_delete=models.CASCADE, related_name='documents')
    title = models.CharField(max_length=255)
    file = models.FileField(upload_to='case_documents/')
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Dokument: {self.title} ({self.case.title})"
    class Meta:
        verbose_name = "Fall-Dokument"
        verbose_name_plural = "Fall-Dokumente"
        ordering = ['-uploaded_at']
#    def save(self, *args, **kwargs):
#        if not self.title:
#            self.title = self.file.name
#        super().save(*args, **kwargs)
#    def get_file_url(self):
#        """Returns the URL of the uploaded file."""
#        return self.file.url if self.file else None
#    def get_case_title(self):
#        """Returns the title of the associated case."""
#        return self.case.title if self.case else "Kein Fall zugeordnet"
#    def get_uploaded_date(self):
#        """Returns the date when the document was uploaded."""
#        return self.uploaded_at.strftime('%Y-%m-%d %H:%M:%S') if self.uploaded_at else "Unbekannt"
#    def is_valid_file_type(self):
#        """Checks if the uploaded file is of a valid type."""
#        valid_file_types = ['application/pdf', 'image/jpeg', 'image/png']
#        return self.file.content_type in valid_file_types if self.file else False
#    def get_file_size(self):
#        """Returns the size of the uploaded file in bytes."""
#        return self.file.size if self.file else 0
#    def delete(self, *args, **kwargs):
#        """Deletes the document and its associated file."""
#        if self.file:
#            self.file.delete(save=False)
#        super().delete(*args, **kwargs)
#    def get_document_info(self):
#        """Returns a dictionary with document information."""
#        return {
#            'title': self.title,
#            'file_url': self.get_file_url(),
#            'uploaded_at': self.get_uploaded_date(),
#            'case_title': self.get_case_title(),
#            'file_size': self.get_file_size(),
#            'is_valid_file_type': self.is_valid_file_type(),
#        }
#    def get_absolute_url(self):
#        """Returns the absolute URL for the document."""
#        return f"/cases/{self.case.id}/documents/{self.id}/"
#    def get_case_url(self):
#        """Returns the URL for the associated case."""
#        return f"/cases/{self.case.id}/"
#    def get_document_summary(self):
#        """Returns a summary of the document."""
#        return f"{self.title} - {self.get_uploaded_date()} ({self.get_case_title()})"
#    def __str__(self):
#        """Returns a string representation of the document."""
#        return f"{self.title} ({self.case.title})"
#    def get_document_type(self):
#        """Returns the type of the document based on its file extension."""
#        return self.file.name.split('.')[-1] if self.file else "Unbekannt"
#    def get_document_size(self):
#        """Returns the size of the document in a human-readable format."""
#        size = self.file.size if self.file else 0
#        if size < 1024:
#            return f"{size} Bytes"
#        elif size < 1024 * 1024:
#            return f"{size / 1024:.2f} KB"
#        elif size < 1024 * 1024 * 1024:
#            return f"{size / (1024 * 1024):.2f} MB"
#        else:
#            return f"{size / (1024 * 1024 * 1024):.2f} GB"
#    def get_document_details(self):
#        """Returns a detailed dictionary with document information."""
#        return {
#            'title': self.title,
#            'file_url': self.get_file_url(),
#            'uploaded_at': self.get_uploaded_date(),
#            'case_title': self.get_case_title(),
#            'file_size': self.get_file_size(),
#            'is_valid_file_type': self.is_valid_file_type(),
#            'document_type': self.get_document_type(),
#            'document_size': self.get_document_size(),
#            'document_summary': self.get_document_summary(),
#            'absolute_url': self.get_absolute_url(),
#            'case_url': self.get_case_url(),
#        }
#    def get_document_metadata(self):
#        """Returns a dictionary with metadata about the document."""
#        return {
#            'title': self.title,
#            'file_url': self.get_file_url(),
#            'uploaded_at': self.get_uploaded_date(),
#            'case_title': self.get_case_title(),
#            'file_size': self.get_file_size(),
#            'is_valid_file_type': self.is_valid_file_type(),
#            'document_type': self.get_document_type(),
#            'document_size': self.get_document_size(),
#            'document_summary': self.get_document_summary(),
#            'absolute_url': self.get_absolute_url(),
#            'case_url': self.get_case_url(),
#            'document_info': self.get_document_info(),
#            'document_details': self.get_document_details(),
#        }
#    def get_document_summary(self):
#        """Returns a summary of the document."""
#        return f"{self.title} - {self.get_uploaded_date()} ({self.get_case_title()})"
#    def get_document_info(self):
#        """Returns a dictionary with document information."""
#        return {
#            'title': self.title,
#            'file_url': self.get_file_url(),
#            'uploaded_at': self.get_uploaded_date(),
#            'case_title': self.get_case_title(),
#            'file_size': self.get_file_size(),
#            'is_valid_file_type': self.is_valid_file_type(),
#            'document_type': self.get_document_type(),
#            'document_size': self.get_document_size(),
#            'document_summary': self.get_document_summary(),
#            'absolute_url': self.get_absolute_url(),
#            'case_url': self.get_case_url(),
#        }