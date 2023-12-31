from django.urls import path
from . import views
from django.contrib.staticfiles.storage import staticfiles_storage
from django.views.generic.base import RedirectView
from django.conf import settings
from django.conf.urls.static import static
app_name = 'pages_prototype'
from . import views


urlpatterns = [
    path('', views.LandingPage.as_view(), name='landing'),
    path('login/', views.LoginPage.as_view(), name='login'),
    path('login', views.LoginPage.as_view(), name='login'),
    path('dashboard', views.DashboardPage.as_view(), name='dashboard'),
    path('dashboard/', views.DashboardPage.as_view(), name='dashboard'),
    path('destination/<str:country>-<str:place>/', views.DestinationPage.as_view(), name='destination'),
    path('destination/<str:country>-<str:place>', views.DestinationPage.as_view(), name='destination'),
    path('destination/<str:country>-<str:place>/stay', views.HotelPage.as_view(), name='hotel'),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)