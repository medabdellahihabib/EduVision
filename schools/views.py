from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from django.urls import reverse_lazy
from django.contrib import messages
from .models import School, Classroom

class SuperAdminRequiredMixin(UserPassesTestMixin):
    def test_func(self):
        return self.request.user.is_authenticated and self.request.user.role == 'superadmin'

class SchoolAdminRequiredMixin(UserPassesTestMixin):
    def test_func(self):
        return self.request.user.is_authenticated and self.request.user.role in ['superadmin', 'school_admin']

class SchoolListView(LoginRequiredMixin, SchoolAdminRequiredMixin, ListView):
    model = School
    template_name = 'schools/list.html'
    context_object_name = 'schools'
    
    def get_queryset(self):
        if self.request.user.role == 'superadmin':
            return School.objects.all()
        elif self.request.user.role == 'school_admin':
            return School.objects.filter(schooladmin__user=self.request.user, schooladmin__is_active=True)

class SchoolCreateView(LoginRequiredMixin, SuperAdminRequiredMixin, CreateView):
    model = School
    template_name = 'schools/create.html'
    fields = ['name', 'code', 'address', 'phone', 'email', 'logo', 'website']
    success_url = reverse_lazy('schools:list')
    
    def form_valid(self, form):
        form.instance.created_by = self.request.user
        messages.success(self.request, 'École créée avec succès!')
        return super().form_valid(form)

class SchoolUpdateView(LoginRequiredMixin, SchoolAdminRequiredMixin, UpdateView):
    model = School
    template_name = 'schools/update.html'
    fields = ['name', 'code', 'address', 'phone', 'email', 'logo', 'website', 'is_active']
    success_url = reverse_lazy('schools:list')
    
    def form_valid(self, form):
        messages.success(self.request, 'École mise à jour avec succès!')
        return super().form_valid(form)

class SchoolDeleteView(LoginRequiredMixin, SuperAdminRequiredMixin, DeleteView):
    model = School
    template_name = 'schools/delete.html'
    success_url = reverse_lazy('schools:list')
    
    def delete(self, request, *args, **kwargs):
        messages.success(self.request, 'École supprimée avec succès!')
        return super().delete(request, *args, **kwargs)

class SchoolDetailView(LoginRequiredMixin, SchoolAdminRequiredMixin, DetailView):
    model = School
    template_name = 'schools/detail.html'
    context_object_name = 'school'