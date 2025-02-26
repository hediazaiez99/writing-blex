# batch_analyses/forms.py
from django import forms

class DocumentUploadForm(forms.Form):
    document1 = forms.FileField(label="Document 1 - Batch Analyses")
    document2 = forms.FileField(label="Document 2 - Analyses du laboratoire")
