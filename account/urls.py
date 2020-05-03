from django.urls import path, include
from . import views
urlpatterns = [
	path('', include('django.contrib.auth.urls')),
	path('main/', views.main, name='account_main'),

]
