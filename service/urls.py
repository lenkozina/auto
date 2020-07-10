from django.urls import path

import service.views as service

app_name = 'service'

urlpatterns = [
    path('', service.index, name='index'),
]    
