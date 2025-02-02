from django.urls import path, include
from .views import faq_view, FAQListView

urlpatterns = [
    path('faqs/', faq_view, name='faq-list'),  # Template-based view
    path('api/faqs/', FAQListView.as_view(), name='faq-list-api'),  # API endpoint
    path('ckeditor5/', include('django_ckeditor_5.urls')),
]
