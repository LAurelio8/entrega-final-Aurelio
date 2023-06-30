from django.urls import path
from entrega_final import views
from django.contrib import admin


urlpatterns = [
    path('signup/', views.signup),
    path('login/', views.login_view),
    path('messages/', views.messages),
    path('index/', views.index),
    path('admin/', admin.site.urls),
]
