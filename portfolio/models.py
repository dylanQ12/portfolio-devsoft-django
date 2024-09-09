from django.db import models
from datetime import date
import os

# Create your models here.
class Project(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)
    image = models.ImageField(upload_to="portfolio/images")
    url_page = models.URLField(null=True, blank=True)
    url_github = models.URLField(null=True, blank=True)
    date = models.DateField(default=date.today)
    
    def __str__(self):
        return f"{self.title}"
    
    def save(self, *args, **kwargs):
        if self.pk:  # Si el objeto ya existe, es una actualización
            old_instance = Project.objects.get(pk=self.pk)
            if old_instance.image and self.image != old_instance.image:
                if os.path.isfile(old_instance.image.path):
                    os.remove(old_instance.image.path)
        super().save(*args, **kwargs)

    def delete(self, *args, **kwargs):
        if self.image:
            if os.path.isfile(self.image.path):
                os.remove(self.image.path)
        super().delete(*args, **kwargs)
    
    
