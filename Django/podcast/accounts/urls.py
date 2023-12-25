from django.urls import path
from accounts.views import PodcastLoginView, logout_view, RegisterView

urlpatterns = [
  path('register/', RegisterView.as_view(), name="register"),
  path('login/', PodcastLoginView.as_view(), name="login"),
  path('logout/', logout_view, name='logout'),
]