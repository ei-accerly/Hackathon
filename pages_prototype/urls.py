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
]