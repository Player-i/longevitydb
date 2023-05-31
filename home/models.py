from django.db import models
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.


class Study(models.Model):
    # In title we write how they benefit from study
    title = models.CharField(max_length=255)

    # Slug is to create the link for them to read the content
    slug = models.SlugField(unique=True, max_length=255)

    # Content is to write what they need to do to benefit
    content = models.TextField()

    # Link is for the link of the study
    link = models.TextField()

    # If the study is about sleep, supplements, diet
    filter = models.CharField(max_length=30)

    def get_absolute_url(self):
        return reverse("study_detail", args=[self.slug])
