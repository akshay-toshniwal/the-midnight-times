import requests
from django.shortcuts import render, redirect
from django.views import View
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import SearchResult
from django.conf import settings  


def fetch_api_response(url, params):
    """
    Fetches API response given the URL and parameters.
    """
    try:
        params["api_token"] = settings.NEWS_API_KEY
        response = requests.get(url, params=params)
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        raise


class SearchView(View):
    template_name = 'search/search.html'
    API_URL = "https://api.thenewsapi.com/v1/news/all"

    def get(self, request):
        return render(request, self.template_name)

    def post(self, request):
        query = request.POST.get('query', '')

        params = {'limit': 1, 'search': query}
        response = fetch_api_response(self.API_URL, params)

        for article in response.get('data', []):
            SearchResult.objects.create(
                search_query=query,
                title=article.get('title', ''),
                description=article.get('description', ''),
                url=article.get('url', ''),
                date_published=article.get('published_at', '')
            )
        return HttpResponseRedirect(reverse('previous_searches'))

class PreviousSearchesView(View):
    template_name = 'search/previous_searches.html'

    def get(self, request):
        search_results = SearchResult.objects.all()
        return render(request, self.template_name, {'searches': search_results})
    
class RefreshResultsView(View):
    API_URL = "https://api.thenewsapi.com/v1/news/all"

    def post(self, request):
        query_id = request.POST.get('query_id')
        search_result = SearchResult.objects.get(pk=query_id)
        
        params = {'limit': 1, 'search': search_result.search_query}
        response  = fetch_api_response(self.API_URL, params)
        if response:
            data = response.get('data')[0]
            search_result.title=data.get('title', '')
            search_result.description=data.get('description', '')
            search_result.url=data.get('url', '')
            search_result.date_published=data.get('published_at', '')
            search_result.save()
        return redirect('previous_searches')

