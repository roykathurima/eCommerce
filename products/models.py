import random
import os
from django.db import models
from django.db.models.signals import pre_save
from django.urls import reverse
from django.db.models import Q
from .utils import unique_slug_generator

def get_filename_ext(filepath):
    base_name = os.path.basename(filepath)
    name, ext = os.path.splitext(base_name)
    return name, ext

def upload_image_path(instance, filename):
    new_filename = random.randint(1,999999999999)
    name, ext = get_filename_ext(filename)
    final_filename = f"{new_filename}{ext}"
    return f"products/{new_filename}/{final_filename}"


class ProductQuerySet(models.query.QuerySet):
    def search(self, query):
        lookup = Q(title__icontains=query) | Q(description__icontains=query)
        return self.filter(lookup).distinct()

class ProductManager(models.Manager):
    def get_queryset(self):
        return ProductQuerySet(self.model, using=self._db)

    def search(self, query):
        return self.get_queryset().all().search(query)

class Product(models.Model):
    title       = models.CharField(max_length=50)
    slug        = models.SlugField(blank=True, unique=True)
    description = models.TextField(blank=True, null=True)
    price       = models.DecimalField(max_digits=10, decimal_places=2)
    featured    = models.BooleanField(default=False)
    image       = models.FileField(null=True, blank=True, upload_to=upload_image_path)

    objects = ProductManager()

    def __str__(self, *args, **kwargs):
    	return self.title

    #they are know as instance methods

    def get_absolute_url(self):
    	#return f"/products/{self.id}"
    	# return reverse("product-detail", kwargs={"id":self.id})
        return reverse("slug-detail", kwargs={"slug":self.slug})

    #This allows for intercheangeability between title and name
    @property
    def name(self):
    	return self.title

def product_pre_save_receiver(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = unique_slug_generator(instance)

pre_save.connect(product_pre_save_receiver, sender=Product)