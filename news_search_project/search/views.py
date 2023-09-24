import requests
from django.urls import reverse, reverse_lazy
from django.shortcuts import render, redirect
from django.views import View
from django.http import HttpResponseRedirect
from django.utils.decorators import method_decorator
from django.views.generic.edit import CreateView
from django.contrib.auth.decorators import login_required
from django.conf import settings
from django.core.cache import cache
from .models import SearchResult
from .forms import CustomUserCreationForm


def fetch_api_response(url, params):
    """
    Fetches API response given the URL and parameters.

    Parameters:
    url (str): The API URL to make the request to.
    params (dict): The parameters to include in the API request.

    Returns:
    list: A list of API response data.
    """


    try:
        params["api_token"] = settings.NEWS_API_KEY
        response = requests.get(url, params=params)
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        raise


class SearchView(View):
    """
    View for handling search requests and storing results.

    Attributes:
    template_name (str): The template to use for rendering the view.
    API_URL (str): The URL for the external API.
    """


    template_name = 'search/search.html'
    API_URL = "https://api.thenewsapi.com/v1/news/all"
    CACHED_TIMEOUT = 900  # 15 minutes in seconds

    def get(self, request):
        """
        Handles GET requests to display the search view.

        Renders the search template.

        Parameters:
        request (HttpRequest): The HTTP request object.

        Returns:
        HttpResponse: Renders the search template.
        """


        return render(request, self.template_name)
    
    @method_decorator(login_required)
    def post(self, request):
        """
        Handles POST requests for the search view.

        This method processes the POST request for a search query.
        It retrieves the query from the request and uses it to make an API request.
        It then processes the API response and stores the search result in the database.

        Parameters:
        request (HttpRequest): The HTTP request object.

        Returns:
        HttpResponseRedirect: Redirects to the previous searches view.
        """


        query = request.POST.get('query', '')

        cache_query = "user_{}_query_{}".format(str(request.user.id), query)
        cached_results = cache.get(cache_query)

        if cached_results:
            return HttpResponseRedirect(reverse('previous_searches'))
        
        params = {'limit': 1, 'search': query}
        response = fetch_api_response(self.API_URL, params)

        for article in response.get('data', []):
            SearchResult.objects.create(
                user = request.user,
                search_query=query,
                title=article.get('title', ''),
                description=article.get('description', ''),
                url=article.get('url', ''),
                date_published=article.get('published_at', '')
            )

        cache.set(cache_query, response, timeout=self.CACHED_TIMEOUT)
        return HttpResponseRedirect(reverse('previous_searches'))

class PreviousSearchesView(View):
    """
    View for previous search results.

    Attributes:
    template_name (str): The template to use for rendering the view.
    """
    

    template_name = 'search/previous_searches.html'

    @method_decorator(login_required)    
    def get(self, request):
        """
        Handles GET requests to display the previous search results.

        Retrieves all search results from the database and renders the
        previous searches template with the search results.

        Parameters:
        request (HttpRequest): The HTTP request object.

        Returns:
        HttpResponse: Renders the previous searches template with the search results.
        """


        search_results = SearchResult.objects.filter(user=request.user)
        return render(request, self.template_name, {'searches': search_results})
    
class RefreshResultsView(View):
    """
    View for refreshing search results.

    Attributes:
    API_URL (str): The URL for the external API.
    """


    API_URL = "https://api.thenewsapi.com/v1/news/all"

    @method_decorator(login_required)
    def post(self, request):
        """
        Handles POST requests for refreshing search results.

        It retrieves the query ID from the request
        and uses it to fetch the corresponding search result.
        It then makes an API request to update the search result details,
        and redirects to the previous searches view.

        Parameters:
        request (HttpRequest): The HTTP request object.

        Returns:
        HttpResponseRedirect: Redirects to the previous searches view.
        """


        query_id = request.POST.get('query_id')
        search_result = SearchResult.objects.get(pk=query_id)
        
        params = {
            'limit': 1,
            'search': search_result.search_query,
            'published_after':search_result.date_published.strftime('%Y-%m-%dT%H:%M:%S')
            }

        response  = fetch_api_response(self.API_URL, params)
        if response:
            data = response.get('data')[0]
            search_result.title=data.get('title', '')
            search_result.description=data.get('description', '')
            search_result.url=data.get('url', '')
            search_result.date_published=data.get('published_at', '')
            search_result.save()
        return redirect('previous_searches')

class SignUpView(CreateView):
    """
    View for user sign-up using a custom user creation form.

    This view extends Django's CreateView to handle user registration.
    It uses a custom user creation form for registration.

    Attributes:
        form_class (type): The form class for user registration.
        success_url (str): The URL to redirect to on successful registration.
        template_name (str): The template to use for rendering the sign-up view.
    
    """
        
    form_class = CustomUserCreationForm
    success_url = reverse_lazy("login")
    template_name = "registration/signup.html"