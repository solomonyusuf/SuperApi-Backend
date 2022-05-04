"""
Definition of urls for SuperApi.
"""
from django.contrib import admin
from django.contrib.auth.views import LoginView, LogoutView
from app import forms, views
from django.urls import include, path
from rest_framework import routers
from django.conf import settings
from django.conf.urls.static import static
from datetime import datetime
from django.urls import path,include


router = routers.DefaultRouter()
router.register(r'api/contact', views.SupernaturalContactViewSet)
router.register(r'api/posts', views.SupernaturalPostViewSet)     
router.register(r'api/sermons', views.SupernaturalSermonViewSet)
router.register(r'api/videos', views.SupernaturalVideoViewSet)
app_name='SuperApi'

urlpatterns = [ 
    
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls')),
    path('', views.home, name='home'),
    path('admin/', admin.site.urls),
    
    path('contact/', views.contact, name='contact'),
    path('about/', views.about, name='about'),
    path('login/',
         LoginView.as_view
         (
             template_name='app/login.html',
             authentication_form=forms.BootstrapAuthenticationForm,
             extra_context=
             {
                 'title': 'Log in',
                 'year' : datetime.now().year,
             }
         ),
         name='login'),
    path('logout/', LogoutView.as_view(next_page='/'), name='logout'),
    
]
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    
    