from django.urls import path
from .views import SearchView, PreviousSearchesView, RefreshResultsView

urlpatterns = [
    path('', SearchView.as_view(), name='search'),
    path('previous_searches/', PreviousSearchesView.as_view(), name='previous_searches'),
    path('refresh_results/', RefreshResultsView.as_view(), name='refresh_results'),
]

