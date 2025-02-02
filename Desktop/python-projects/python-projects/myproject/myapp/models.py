from django.db import models
from django_ckeditor_5.fields import CKEditor5Field
from googletrans import Translator

translator = Translator()


class FAQ(models.Model):
    question = models.TextField()
    # answer = RichTextField()
    
    # Language-specific fields
    # question_hi = models.TextField(blank=True, null=True)
    # answer_hi = RichTextField(blank=True, null=True)
    
    # answer_bn = RichTextField(blank=True, null=True)
    answer = CKEditor5Field('Answer')
    question_hi = CKEditor5Field('Question in Hindi',blank=True,null=True)
    question_bn = CKEditor5Field('Question in Bengali',blank=True,null=True)
    answer_hi = CKEditor5Field('Answer in Hindi', blank=True, null=True)
    answer_bn = CKEditor5Field('Answer in Bengali', blank=True, null=True)

    def __str__(self):
        return self.question

    @staticmethod
    def translate_text(text, target_language):
        """Translate text to the target language using Google Translate."""
        try:
            translation = translator.translate(text, dest=target_language)
            return translation.text
        except Exception as e:
            print(f"Translation failed: {e}")
            return text  # Fallback to original text

    def save(self, *args, **kwargs):
        """Automatically translate question and answer before saving."""
        if not self.question_hi:
            self.question_hi = self.translate_text(self.question, "hi")
        if not self.answer_hi:
            self.answer_hi = self.translate_text(self.answer, "hi")
        if not self.question_bn:
            self.question_bn = self.translate_text(self.question, "bn")
        if not self.answer_bn:
            self.answer_bn = self.translate_text(self.answer, "bn")

        super().save(*args, **kwargs)

    def get_translated_question(self, lang_code):
        """Get translated question based on language code."""
        return getattr(self, f"question_{lang_code}", self.question) or self.question

    def get_translated_answer(self, lang_code):
        """Get translated answer based on language code."""
        return getattr(self, f"answer_{lang_code}", self.answer) or self.answer
