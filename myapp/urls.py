from django.contrib import admin
from django.urls import path
from myapp import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('hospitals/', views.hospitals, name='hospitals'),
    path('learn/', views.learn, name='learn'),
    path('blog/', views.blog, name='blog'),
    path('contact/', views.contact, name='contact'),
    path('admin/', admin.site.urls),
    path('hospitals/', views.hospital_list, name='hospital_list'),
    path('hospitals/create/', views.hospital_create, name='hospital_create'),
    path('hospitals/<int:pk>/edit/', views.hospital_edit, name='hospital_edit'),
    path('hospitals/<int:pk>/delete/', views.hospital_delete, name='hospital_delete'),
]