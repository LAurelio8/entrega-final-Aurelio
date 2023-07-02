from django import forms
from .models import Message

class MessageForm(forms.ModelForm):
    class Meta:
        model = Message
        fields = ['receiver', 'subject', 'content']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['receiver'].label = 'Destinatario'
        self.fields['subject'].label = 'Asunto'
        self.fields['content'].label = 'Contenido del mensaje'
