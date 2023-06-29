from django.shortcuts import render, redirect
from django.urls import reverse
from django.core.mail import EmailMessage
from .forms import ContactForm

# Create your views here.

def contact(request):
    #print(f"Tipo de Petición: {request.method}")
    contact_form = ContactForm()

    if request.method == 'POST':
        contact_form = ContactForm(data=request.POST)

        if contact_form.is_valid():
            name     =  request.POST.get('name', '')  # si no hay nada, no devuelve nada
            email    =  request.POST.get('email', '')
            content  =  request.POST.get('content', '')

            # Todo anda bien

            # Enviamos el correo
            email = EmailMessage(
                "La Caffettiera: Nuevo mensaje de contacto",  # asunto
                f"De {name} <{email}>\n\nEscribió:\n\n{content}",  # cuerpo
                "no-contestar@inbox.mailtrap.io",  # origen
                ["maikitoprogramando@gmail.com"], # destino
                reply_to=[email]
            )

            try:
                email.send()
                # Redireccionamos a OK
                return redirect(reverse('contact') + '?ok')  # utiliza el nombre
            except:
                # Redireccionamos a FAIL
                return redirect(reverse('contact') + '?fail')
        
    return render(request, 'contact/contact.html', {'form': contact_form})
