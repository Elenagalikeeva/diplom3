"""
URL configuration for kam_proj project.

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
from django.conf.urls.static import static
from django.conf import settings
from kam import views



urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('blog/', views.blogs, name='blogs'),
    path('<int:blog_id>/', views.detail, name='detail'),
    path('signup/', views.signupuser, name='signupuser'),
    path('kabinet/', views.kabinet, name='kab'),
    path('logout/', views.logoutuser, name='logoutuser'),
    path('login/', views.loginuser, name='loginuser'),
    path('vosho/', views.vosho, name='vosho'),
    path('more/', views.more, name='more'),
    path('obzor/', views.obzor, name='obzor'),
    path('vse/', views.vse, name='vse'),
    path('thanks/', views.thanks_page, name='thanks_page'),
    path('carusel/', views.carusel, name='products'),
    path('leave_review/', views.leave_review, name='leave_review'),

]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
