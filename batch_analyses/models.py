# batch_analyses/models.py
from django.db import models

class Document(models.Model):
    title = models.CharField(max_length=255)
    uploaded_file = models.FileField(upload_to='documents/')
    upload_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

# batch_analyses/models.py
from django.db import models

class ValidatedDocuments(models.Model):
    doc1 = models.FileField(upload_to='validated/')
    doc2 = models.FileField(upload_to='validated/')
    updated_doc = models.FileField(upload_to='validated/')
    validated_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Validation du {self.validated_at.strftime('%Y-%m-%d %H:%M:%S')}"
