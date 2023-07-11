from .import views
from django.urls import path

urlpatterns = [
      path('',views.demo,name='demo'),
      # path('pan',views.demo_panel,name='demo_panel'),
      
]     
