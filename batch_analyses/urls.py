from django.urls import path
from . import views
from .views import upload_documents, home, delete_document

urlpatterns = [
    path('', home, name='home'),
    path('upload/', upload_documents, name='upload_documents'),
    path('delete/<int:doc_id>/', delete_document, name='delete_document'),
]