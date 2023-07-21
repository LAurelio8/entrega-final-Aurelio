from django.urls import path
from entrega_final import views
from django.contrib import admin

urlpatterns = [
    path('signup/', views.signup),
    path('login/', views.login_view, name='login'),
    path('messages/', views.messages, name='messages'),
    path('index/', views.index),
    path('admin/', admin.site.urls),
    path('about/', views.about, name='about'),
    path('portfolio/', views.portfolio, name='portfolio'),
]
