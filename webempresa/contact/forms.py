from django import forms

class ContactForm(forms.Form):
    name = forms.CharField(label='nombre', required=True, widget=forms.TextInput(
        attrs = {'class' : 'form-control'}
    ), min_length=10, max_length=100)
    email = forms.EmailField(label='email', required=True, widget=forms.TextInput(
        attrs = {'class' : 'form-control', 'placeholder' : 'Escribe tu Mail'}
    ), min_length=10, max_length=100)
    content = forms.CharField(label='contenido', required=True, widget = forms.Textarea(
        attrs = {'class' : 'form-control', 'rows': 3, 'placeholder' : 'Escribe tu mensaje'}
    ), min_length=10, max_length=100)
