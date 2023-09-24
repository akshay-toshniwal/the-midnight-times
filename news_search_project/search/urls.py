from django.urls import path
from django.contrib.auth.views import LoginView
from .views import SearchView, PreviousSearchesView, RefreshResultsView, SignUpView

urlpatterns = [
    path('', SearchView.as_view(), name='search'),
    path('login/', LoginView.as_view(), name='login'),
    path("signup/", SignUpView.as_view(), name="signup"),
    path('previous_searches/', PreviousSearchesView.as_view(), name='previous_searches'),
    path('refresh_results/', RefreshResultsView.as_view(), name='refresh_results'),
]

