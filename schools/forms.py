from django import forms
from .models import School, Classroom

class SchoolForm(forms.ModelForm):
    class Meta:
        model = School
        fields = ['name', 'code', 'address', 'phone', 'email', 'logo', 'website', 'is_active']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nom de l\'école'}),
            'code': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Code unique'}),
            'address': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'phone': forms.TextInput(attrs={'class': 'form-control', 'placeholder': '+33 ...'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'contact@ecole.fr'}),
            'website': forms.URLInput(attrs={'class': 'form-control', 'placeholder': 'https://...'}),
        }

class ClassroomForm(forms.ModelForm):
    class Meta:
        model = Classroom
        fields = ['school', 'name', 'code', 'capacity', 'location', 'description']
        widgets = {
            'school': forms.Select(attrs={'class': 'form-control'}),
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'code': forms.TextInput(attrs={'class': 'form-control'}),
            'capacity': forms.NumberInput(attrs={'class': 'form-control'}),
            'location': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
        }