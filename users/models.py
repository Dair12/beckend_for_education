from django.db import models
from django.contrib.auth.hashers import make_password

class User(models.Model):
    ROLE_CHOICES = (
        ('User', 'User'),
        ('Admin', 'Admin'),
        ('SysAdmin', 'SysAdmin'),
    )

    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    password_hash = models.CharField(max_length=255)
    role = models.CharField(max_length=50, choices=ROLE_CHOICES)
    created_at = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        # Хеширование пароля перед сохранением
        if self.password_hash and not self.password_hash.startswith('pbkdf2_sha256'):
            self.password_hash = make_password(self.password_hash)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.email

    class Meta:
        db_table = 'users'