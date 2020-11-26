from django.shortcuts import render, redirect
#Importo desde form a la vista para mostrarlo
from .forms import ContactForm
from django.urls import reverse
from django.core.mail import EmailMessage


# Create your views here.
def contacto (request): 
    contact_form = ContactForm() #Aquí lo instanciamos(ponerlo como variable de la función )
#Para validar, se creó el formulario vacio (conatc_form), ahora verifico si el método del request es POST,
# si es así y es válido (están bien cargados) recupero los campos con los métodos de request    
    if request.method== "POST":
        contact_form = ContactForm (data=request.POST)
        if contact_form.is_valid():
            name = request.POST.get ('name', '')
            email = request.POST.get ('email', '')
            content = request.POST.get ('content', '')
#Ahora debo mostrarle al usuario que el formulario fue enviado correctamente, importo redirect y hago lo siguiente,
#pero en lugar de pasarle /contact/ en crudo, importamos reverse para pasarle el nombre de la url como lo hacemos,
#con un tag url, esto es en primera instancia, luego cuando configuramos el email, debemos enviarlo, importamos  EmailMessage
            email = EmailMessage(
                "Vanesa Fernandez: Nuevo mensaje de contacto",
                "De {} <{}>\n\nEscribió:\n\n{}".format(name, email, content),
                "no-contestar@gmail.com",
                ["nicodoffo2015@gmail.com"],
                reply_to=[email]
            )

            try:  
                email.send()
                return redirect(reverse('contact')+"?ok")
                

            except:
                #Algo na ha ido bien, redireccionamos a FAIL   
                return redirect(reverse('contact')+"?fail")
                
            

    #Entonces ahora lo mandamos al template con un diccionario de contexto.

    if 'fail' in request.GET:
        return render (request, "contact/mensaje_error.html")
    else:
        return render (request, "contact/contact.html", {'form':contact_form})
        


        



    
