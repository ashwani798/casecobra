from rest_framework import serializers
from .models import FAQ

class FAQSerializer(serializers.ModelSerializer):
    question = serializers.SerializerMethodField()
    answer = serializers.SerializerMethodField()

    class Meta:
        model = FAQ
        fields = ['id', 'question', 'answer']

    def get_question(self, obj):
        """Get translated question based on request language."""
        lang_code = self.context.get('request').query_params.get('lang', 'en')
        return obj.get_translated_question(lang_code)

    def get_answer(self, obj):
        """Get translated answer based on request language."""
        lang_code = self.context.get('request').query_params.get('lang', 'en')
        return obj.get_translated_answer(lang_code)
