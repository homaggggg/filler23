from django.urls import reverse #Used to generate URLs by reversing the URL patterns
from django.db import models
import uuid

class Doc(models.Model):
    title = models.CharField(max_length=200)
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, help_text="Unique ID")
    createdate = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.title


    def get_absolute_url(self):
        return reverse('doc-detail', args=[str(self.id)])

