from django.contrib import admin
from django.urls import path
from tasks.views import *
urlpatterns = [
    path('admin/', admin.site.urls),
    path("login/", CustomLoginView.as_view(), name="login"),
    path("register/", RegisterPage.as_view(), name="register"),
    path('tasks/', TaskListView.as_view(), name='task-list'),
    path('tasks/create/', TaskCreateView.as_view(), name='task-create'),
    path('tasks/edit/<int:pk>/', TaskEditView.as_view(), name='task-edit'),
    path('tasks/delete/<int:pk>/', TaskDeleteView.as_view(), name='task-delete'),
    path('tasks/confirm/<int:pk>/', TaskDoneView.as_view(), name='task-done'),
]
