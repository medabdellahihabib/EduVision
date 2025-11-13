from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.db import models

# Manager personnalisé pour gérer la création d'utilisateurs et superutilisateurs
class UserManager(BaseUserManager):
    use_in_migrations = True

    def create_user(self, username, email=None, password=None, **extra_fields):
        if not username:
            raise ValueError("Le username doit être défini")
        email = self.normalize_email(email)
        user = self.model(username=username, email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, email=None, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('role', 'admin_global')

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser doit avoir is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser doit avoir is_superuser=True.')

        return self.create_user(username, email, password, **extra_fields)


class User(AbstractUser):
    ROLE_CHOICES = [
        ('admin_global', 'Administrateur Global'),
        ('admin_ecole', 'Administrateur École'),
        ('enseignant', 'Enseignant'),
        ('etudiant', 'Étudiant'),
    ]
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default='etudiant')

    objects = UserManager()

    def __str__(self):
        return f"{self.username} ({self.role})"
