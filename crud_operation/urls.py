"""
URL configuration for crud_operation project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from crud import views
urlpatterns = [
    path('', views.add_show, name="addandshow"),            
    path('delete/student/<int:id>', views.deleteStudent, name='delete_student'),
    path('update/student/<int:id>', views.studentUpdate, name='update_student'),
    path('admin/', admin.site.urls),
]
