from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from employees import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.EmployeeList.as_view(), name='list'),
    path('add/', views.EmployeeCreate.as_view(), name='add'),
    path('edit/<int:pk>/', views.EmployeeUpdate.as_view(), name='edit'),
    path('delete/<int:pk>/', views.EmployeeDelete.as_view(), name='delete'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) 
