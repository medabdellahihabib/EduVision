from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.conf import settings  # Import settings to access TEMPLATES

class LoginView(View):
    template_name = 'accounts/login.html'

    def get(self, request):
        # Debug code to check template paths
        template_dirs = settings.TEMPLATES[0]['DIRS']
        print("Looking for template:", self.template_name)
        print("Template directories:", [str(dir) for dir in template_dirs])
        
        # Check if template exists
        import os
        for template_dir in template_dirs:
            template_path = os.path.join(template_dir, self.template_name)
            print(f"Checking: {template_path} -> Exists: {os.path.exists(template_path)}")
        
        return render(request, self.template_name)

    def post(self, request):
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect('accounts:dashboard')
        return render(request, self.template_name, {'error': 'Nom utilisateur ou mot de passe incorrect'})

class LogoutView(View):
    def get(self, request):
        logout(request)
        return redirect('accounts:login')

class DashboardView(LoginRequiredMixin, View):
    template_name = 'accounts/dashboard.html'

    def get(self, request):
        return render(request, self.template_name, {'role': request.user.role})