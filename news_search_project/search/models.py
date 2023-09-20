from django.db import models

class SearchResult(models.Model):
    """
    Model representing a search result.

    Attributes:
    search_query (str): The search query associated with this result.
    title (str): The title of the article.
    description (str): A brief description of the article.
    url (str): The URL of the article.
    date_published (datetime): The date and time the article was published.

    Methods:
    __str__(): Returns a string representation of the search result.
    """

    
    search_query = models.CharField(max_length=255)
    title = models.CharField(max_length=255)
    description = models.TextField()
    url = models.URLField()
    date_published = models.DateTimeField()

    def __str__(self):
        return self.title
