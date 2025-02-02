from django.contrib import admin
from .models import FAQ

class FAQAdmin(admin.ModelAdmin):
    list_display = ('id', 'question', 'get_question_hi', 'get_question_bn')  # Use methods instead of fields
    list_filter = ('question',)  # Only use real fields here

    def get_question_hi(self, obj):
        return obj.get_translated_question('hi')  # Fetch translated text
    get_question_hi.short_description = "Question (Hindi)"

    def get_question_bn(self, obj):
        return obj.get_translated_question('bn')  # Fetch translated text
    get_question_bn.short_description = "Question (Bengali)"

admin.site.register(FAQ, FAQAdmin)
