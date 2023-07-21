from django.db import models
from django.contrib.auth.models import AbstractUser, User


class User(AbstractUser):
    email = models.EmailField(unique=True)
    groups = models.ManyToManyField(
        'auth.Group',
        related_name='custom_user_set',
        blank=True,
        help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.',
        verbose_name='groups',
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='custom_user_set',
        blank=True,
        help_text='Specific permissions for this user.',
        verbose_name='user permissions',
    )

    def __str__(self):
        return self.username

    class Meta:
        app_label = 'entrega_final'
        default_related_name = 'custom_user_set'


class Login(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    is_admin = models.BooleanField(default=False)

    def __str__(self):
        return self.user.username


class Message(models.Model):
    sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name='sent_messages')
    receiver = models.ForeignKey(User, on_delete=models.CASCADE, related_name='received_messages')
    subject = models.CharField(max_length=200)
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

class VerMas(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()

    @property
    def has_long_content(self):
        words = self.content.split()
        return len(words) > 10

    def __str__(self):
        return self.title

class Photo(models.Model):
    image = models.ImageField(upload_to='photos/')
    title = models.CharField(max_length=200)
    description = models.TextField()
    uploaded_at = models.DateTimeField(auto_now_add=True)
    more_detail = models.OneToOneField(VerMas, on_delete=models.CASCADE, null=True, blank=True)  # Corregir aquí

    def __str__(self):
        return self.title


class Text(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
