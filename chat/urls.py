from django.contrib.auth import views as auth_views
from django.urls import path

from . import views
from .views import logout_view
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', views.frontpage, name='frontpage'),
    path('signup/', views.signup, name='signup'),
    path('login/', auth_views.LoginView.as_view(template_name='chat/login.html'), name='login'),
    path('logout/', logout_view, name='logout'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
