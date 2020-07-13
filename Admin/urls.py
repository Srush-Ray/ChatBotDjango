from django.urls import path

from . import views

urlpatterns = [
    path('home/', views.home, name = 'home'),
    path('', views.admin_form, name = 'insert'),
    path('admin_list/', views.admin_list, name = 'display'),
    path('admin_list_unsatis/', views.admin_list_unsat, name = 'display_unsatis'),
    path('<int:id>/', views.admin_form, name = 'update'),
    path('admin_delete/<int:id>/', views.admin_delete, name = 'delete')
]