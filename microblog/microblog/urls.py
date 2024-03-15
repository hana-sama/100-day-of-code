"""
URL configuration for microblog project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.urls import path, include
from blog.views import BlogListView, BlogDetailView, BlogCreateView, BlogUpdateView, BlogDeleteView
from django.contrib.auth.views import LoginView, LogoutView
# Request -> urls.py -> views -> templates -> response -> browser
urlpatterns = [
    # path('<URL>', views(function), name='')
    path('admin/', admin.site.urls),
    # path('', include('microblog.urls')),
    path('', BlogListView.as_view(), name='index'),
    # Int = integer(整数), pk = primary key
    path('<int:pk>', BlogDetailView.as_view(), name='detail'),
    path('create', BlogCreateView.as_view(), name='create'),
    path('<int:pk>/update', BlogUpdateView.as_view(), name='update'),
    path('<int:pk>/delete', BlogDeleteView.as_view(), name='delete'),
    # path('login', LoginView.as_view(template_name='login.html'), name='login'),
    # path('logout/', LogoutView.as_view(http_method_names=["post", "get", "options"]), name='logout'),
    path('userauth/', include('django.contrib.auth.urls')),
    path('userauth/', include('userauth.urls')),
    
]
