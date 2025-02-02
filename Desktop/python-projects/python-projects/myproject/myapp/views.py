from django.shortcuts import render
from rest_framework.generics import ListAPIView
from .models import FAQ
from .serializers import FAQSerializer

# Template-based FAQ View
def faq_view(request):
    language_code = request.GET.get('lang', 'en')  # Get language from query params
    faqs = FAQ.objects.all()
    return render(request, 'faq.html', {'faqs': faqs, 'language_code': language_code})

# API View for FAQs
class FAQListView(ListAPIView):
    queryset = FAQ.objects.all()
    serializer_class = FAQSerializer

    def get_serializer_context(self):
        """Pass request context for dynamic translations"""
        return {'request': self.request}

