# entrega-final-Aurelio

Funcionalidades
Esta aplicación de Django proporciona las siguientes funcionalidades:

Registro de usuarios
La función signup en el archivo views.py maneja el registro de nuevos usuarios. Los usuarios pueden completar un formulario con su nombre de usuario, correo electrónico y contraseña para crear una cuenta. Si el correo electrónico ya está registrado, se mostrará un mensaje de error.

Inicio de sesión
La función login_view en el archivo views.py maneja el inicio de sesión de los usuarios. Los usuarios pueden ingresar su nombre de usuario y contraseña en un formulario para acceder a la aplicación. Si los datos de inicio de sesión son incorrectos, se mostrará un mensaje de error.

Mensajería
La función messages en el archivo views.py maneja la funcionalidad de mensajería de la aplicación. Los usuarios autenticados pueden enviar y recibir mensajes a través de un formulario. Los mensajes recibidos y enviados se muestran en la página de mensajes.

Gestión de fotos
Las funciones create_photo, edit_photo y delete_photo en el archivo views.py manejan la gestión de fotos de la aplicación. Solo los superusuarios pueden acceder a estas funciones. Los superusuarios pueden crear, editar y eliminar fotos mediante formularios.

Estructura del proyecto
El proyecto de Django tiene la siguiente estructura de archivos:

views.py: Contiene las funciones de vista que manejan las solicitudes del cliente.
models.py: Define los modelos de base de datos utilizados en la aplicación.
forms.py: Contiene las definiciones de formularios utilizados en la aplicación.
templates/: Directorio que contiene las plantillas HTML utilizadas para renderizar las vistas.
static/: Directorio que contiene los archivos estáticos, como CSS y JavaScript.
urls.py: Archivo de configuración de URL que mapea las URL a las funciones de vista correspondientes.
