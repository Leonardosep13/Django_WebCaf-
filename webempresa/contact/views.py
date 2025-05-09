from django.shortcuts import render, redirect
from django.urls import reverse
from django.core.mail import EmailMessage
from .forms import ContactForm

def contact(request):
    contact_form = ContactForm()

    if request.method == "POST":
        contact_form = ContactForm(data=request.POST)
        if contact_form.is_valid():
            # Procesar el formulario si es válido, se obtienen las credenciales con un get y se guardan en una variable cada una
            name = contact_form.cleaned_data.get('name', '')
            email = contact_form.cleaned_data.get('email', '')
            content = contact_form.cleaned_data.get('content', '')
            #Enviar el email
            email=EmailMessage(
                "La Caffettiera : Nuevo mensaje de contacto",
                "De {} <{}> \n\n Escribio: \n\n {}".format (name,email,content),
                "no-contestar@inbox.mailtrap.io",
                ["jaime.rios5609@alumnos.udg.mx"],
                reply_to=[email]
            )
            try:
                email.send()
            except:
                return redirect(reverse('contact') + "?fail")
            
            return redirect(reverse('contact') + "?ok")
            
    return render(request, "contact/contact.html", {'form': contact_form})


