from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as auth_login 
from .models import User, Login, Message
from .forms import MessageForm
from django.db import IntegrityError
from django.contrib.auth.decorators import login_required, user_passes_test


def signup(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        
        try:
            User.objects.create_user(username=username, email=email, password=password)
            return redirect('login')
        except IntegrityError:
            error_message = 'El correo electrónico ya está registrado.'
            return render(request, 'signup.html', {'error_message': error_message})
    
    return render(request, 'signup.html')

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        if username == 'usuario' and password == 'contraseña':
            # Datos de inicio de sesión correctos
            return render(request, 'login.html', {'login_successful': True})
        else:
            # Datos de inicio de sesión incorrectos
            return render(request, 'login.html', {'login_successful': False})
    else:
        return render(request, 'login.html')

def messages(request):
    # Lógica para manejar la app de mensajería
    return render(request, 'messages.html')

def about(request):
    about_info = About.objects.all()
    return render(request, 'about.html', {'about_info': about_info})

@login_required
@user_passes_test(lambda user: user.is_superuser, login_url='login')
def create_photo(request):
    if request.method == 'POST':
        # Procesar los datos enviados en el formulario de creación de fotos
        # y guardar la foto en la base de datos
        return redirect('photos')  # Redirigir a la página de fotos
    return render(request, 'create_photo.html')

@login_required
@user_passes_test(lambda user: user.is_superuser, login_url='login')
def edit_photo(request, photo_id):
    photo = Photo.objects.get(id=photo_id)
    if request.method == 'POST':
        # Procesar los datos enviados en el formulario de edición de la foto
        # y actualizar la foto en la base de datos
        return redirect('photos')  # Redirigir a la página de fotos
    return render(request, 'edit_photo.html', {'photo': photo})

@login_required
@user_passes_test(lambda user: user.is_superuser, login_url='login')
def delete_photo(request, photo_id):
    photo = Photo.objects.get(id=photo_id)
    # Verificar si el usuario tiene permiso para eliminar la foto
    if request.method == 'POST':
        # Eliminar la foto de la base de datos
        return redirect('photos')  # Redirigir a la página de fotos
    return render(request, 'delete_photo.html', {'photo': photo})

def messages(request):
    if request.method == 'POST':
        form = MessageForm(request.POST)
        if form.is_valid():
            message = form.save(commit=False)
            message.sender = request.user
            message.save()
            return redirect('messages')
    else:
        form = MessageForm()
    
    received_messages = Message.objects.filter(receiver=request.user)
    sent_messages = Message.objects.filter(sender=request.user)
    
    context = {
        'form': form,
        'received_messages': received_messages,
        'sent_messages': sent_messages
    }
    return render(request, 'messages.html', context)

def index(request):
    return render(request, 'index.html')