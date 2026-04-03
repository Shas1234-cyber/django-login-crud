from django.urls import path
from . import views

urlpatterns = [
    path('', views.login_view, name='login'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('add/', views.add_student, name='add'),
    path('update/<int:id>/', views.update_student, name='update'),
    path('delete/<int:id>/', views.delete_student, name='delete'),
    path('logout/', views.logout_view, name='logout'),
]