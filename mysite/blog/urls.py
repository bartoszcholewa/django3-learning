from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    # Widok posta
    #path('', views.post_list, name='post_list'),
    path('', views.PostListView.as_view(), name='post_list'),
    # Konwertery ścieżki: https://docs.djangoproject.com/en/3.2/topics/http/urls/#path-converters
    path('<int:year>/<int:month>/<int:day>/<slug:post>/', views.post_detail, name='post_detail'),
]