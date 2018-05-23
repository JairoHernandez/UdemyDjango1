from django.conf.urls import url
from . import views

# organize urls based on app name
# <form method="POST" action="{% url 'accounts:loginview' %}">
app_name = 'posts'

urlpatterns = [
    url(r'^create/', views.create, name='create'),
]