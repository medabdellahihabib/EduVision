from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.mixins import LoginRequiredMixin



class LoginView(View):
    template_name = 'accounts/login.html'  # <-- juste relatif au dossier templates

    def get(self, request):
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
