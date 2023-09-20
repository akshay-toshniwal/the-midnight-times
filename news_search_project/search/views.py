import requests
from django.shortcuts import render, redirect
from django.views import View
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import SearchResult


class SearchView(View):
    template_name = 'search/search.html'

    def get(self, request):
        return render(request, self.template_name)

    def post(self, request):
        query = request.POST.get('query', '')

        params = {'api_token': 'IVXtTaziYiHqSgUizaYabO0DQxBcIz0n6im1uVOg', 'limit': 1, 'search': query}
        response  = requests.get("https://api.thenewsapi.com/v1/news/all", params=params)
        data = response.json()

        for article in data.get('data', []):
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
    def post(self, request):
        query_id = request.POST.get('query_id')
        search_result = SearchResult.objects.get(pk=query_id)
        
        params = {'api_token': 'IVXtTaziYiHqSgUizaYabO0DQxBcIz0n6im1uVOg', 'limit': 1, 'search': search_result.search_query}
        response  = requests.get("https://api.thenewsapi.com/v1/news/all", params=params)
        if response:
            data = response.json()['data'][0]
            search_result.title=data.get('title', '')
            search_result.description=data.get('description', '')
            search_result.url=data.get('url', '')
            search_result.date_published=data.get('published_at', '')
            search_result.save()
        return redirect('previous_searches')

