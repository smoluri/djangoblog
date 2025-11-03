from django.urls import path
from django.conf.urls.static import static
from blog import views


urlpatterns = [
    path('', views.post_list, name='post_list'),
]

