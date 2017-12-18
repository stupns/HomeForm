from django import forms
from AppForm.models import Message


class MessageForm(forms.ModelForm):
    class Meta:
        model = Message
        fields = [
            'mes_title',
            'mes_text',
        ]

