from django.db import models

class SearchResult(models.Model):
    search_query = models.CharField(max_length=255)
    title = models.CharField(max_length=255)
    description = models.TextField()
    url = models.URLField()
    date_published = models.DateTimeField()

    def __str__(self):
        return self.title
