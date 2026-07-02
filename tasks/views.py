from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import DeleteView, ListView, UpdateView, CreateView, View
from django.views.generic.edit import FormView
from django.contrib.auth.views import LoginView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from .models import Task
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import TaskEditForm

class TaskListView(LoginRequiredMixin, ListView):
    model = Task
    template_name = 'tasks_list.html'
    context_object_name = 'tasks'
    ordering = '-id'

    def get_queryset(self):
        return self.model.objects.filter(user=self.request.user)


class TaskCreateView(LoginRequiredMixin, CreateView):
    model = Task
    fields = ['content']
    success_url = '/tasks/'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(TaskCreateView, self).form_valid(form)

class TaskEditView(LoginRequiredMixin, UpdateView):
    model = Task
    form_class = TaskEditForm
    success_url = '/tasks/'

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)

class TaskDeleteView(LoginRequiredMixin, DeleteView):
    model = Task
    context_object_name = "task"
    success_url = reverse_lazy('task-list')

    def get(self, request, *args, **kwargs):
        return self.post(request, *args, **kwargs)
    
    def get_queryset(self):
        return self.model.objects.filter(user=self.request.user)


class TaskDoneView(LoginRequiredMixin, View):
    model = Task
    success_url = reverse_lazy("task-list")

    def get(self, request, *args, **kwargs):
        object = Task.objects.get(id=kwargs.get('pk'))
        object.done = True
        object.save()
        return redirect(self.success_url)
    



class CustomLoginView(LoginView):
    
    template_name = 'login.html'
    fields = "username","password"
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse_lazy('task-list')
    

class RegisterPage(FormView):
    template_name = 'register.html'
    form_class = UserCreationForm
    redirect_authenticated_user = True
    success_url = reverse_lazy('task-list')

    def form_valid(self, form):
        user = form.save()
        if user is not None:
            login(self.request, user)
        return super(RegisterPage, self).form_valid(form)
    
    def get(self, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect("task-list")
        return super(RegisterPage, self).get(*args, **kwargs)