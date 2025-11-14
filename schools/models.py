from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class School(models.Model):
    name = models.CharField(max_length=200)
    code = models.CharField(max_length=20, unique=True)
    address = models.TextField()
    phone = models.CharField(max_length=20)
    email = models.EmailField()
    logo = models.ImageField(upload_to='schools/logos/', null=True, blank=True)
    website = models.URLField(blank=True)
    is_active = models.BooleanField(default=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='schools_created')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        db_table = 'schools'
        verbose_name = 'École'
        verbose_name_plural = 'Écoles'
    
    def __str__(self):
        return self.name

class Classroom(models.Model):
    school = models.ForeignKey(School, on_delete=models.CASCADE, related_name='classrooms')
    name = models.CharField(max_length=100)
    code = models.CharField(max_length=20, unique=True)
    capacity = models.IntegerField(default=30)
    location = models.CharField(max_length=100, blank=True)
    description = models.TextField(blank=True)
    is_active = models.BooleanField(default=True)
    
    class Meta:
        db_table = 'classrooms'
        verbose_name = 'Salle de classe'
        verbose_name_plural = 'Salles de classe'
    
    def __str__(self):
        return f"{self.name} - {self.school.name}"