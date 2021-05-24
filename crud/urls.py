from django.contrib import admin
from django.urls import path
import blog.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', blog.views.main, name='main'),
    path('<str:id>', blog.views.detail, name="detail"),
    path('write/', blog.views.write, name='write'),
    path('write/create/', blog.views.create, name='create'),
    path('edit/<str:id>', blog.views.edit, name="edit"),
    path('update/<str:id>', blog.views.update, name="update"),
    path('delete/<str:id>', blog.views.delete, name="delete"),
]   
