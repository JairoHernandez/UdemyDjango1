from django.conf.urls import url
from . import views

# organize urls based on app name
# <form method="POST" action="{% url 'accounts:loginview' %}">
app_name = 'accounts'

urlpatterns = [
    url(r'^signup/', views.signup, name='signup'),
    url(r'^login/', views.loginview, name='loginview'),
]