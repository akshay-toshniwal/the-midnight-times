from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    """
    Model representing a custom user in the application.

    This model extends the AbstractUser class from Django, adding custom
    attributes and methods to enhance functionality and behavior.

    Attributes:
        is_blocked (bool): A boolean indicating whether the user is blocked or unblocked.

    Methods:
        __str__(): Returns a string representation of the username.
    
    """
    
    
    is_blocked =  models.BooleanField(default=False)

    def __str__(self):
        return self.username

class SearchResult(models.Model):
    """
    Model representing a search result.

    Attributes:
    search_query (str): The search query associated with this result.
    title (str): The title of the article.
    description (str): A brief description of the article.
    url (str): The URL of the article.
    date_published (datetime): The date and time the article was published.
    language (str): The language of article.
    source (str): The URL of source.
    categories (str): The category of article.

    Methods:
    __str__(): Returns a string representation of the search result.
    """

    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    search_query = models.CharField(max_length=255, unique=True)
    title = models.CharField(max_length=255)
    description = models.TextField()
    url = models.URLField()
    date_published = models.DateTimeField()
    language =  models.CharField(max_length=15)
    source = models.URLField()
    categories = models.CharField(max_length=30)

    def __str__(self):
        return self.title
