from django.urls import path
from entrega_final import views

urlpatterns = [
    path('signup/', views.signup),
    path('login/', views.login_view),
    path('admin/', views.admin),
    path('messages/', views.messages),
    path('index/', views.index),
]
