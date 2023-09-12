from django.db import models
from datetime import date
from autoslug import AutoSlugField
from django.core.validators import MaxValueValidator, MinValueValidator


class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

class Person(BaseModel):
    name = models.CharField(max_length=255)
    icon = models.ImageField(upload_to='icon')
    dob = models.DateField(blank=True, null=True)
    about = models.TextField(blank=True, null=True)

    @property
    def age(self):
        if not self.dob:
            return None
        
        today = date.today
        return today.year - self.dob.year - ((today.month, today.day) < (self.dob.month, self.dob.day))


class Category(BaseModel):
    name = models.CharField(max_length=255)
    slug = AutoSlugField(populate_from='name')

    def __str__(self):
        return self.name
    
class MovieType(BaseModel):
    name = models.CharField(max_length=255)
    slug = AutoSlugField(populate_from='name')

    def __str__(self):
        return self.name
    
class Movie(BaseModel):
    name = models.CharField(max_length=255)
    slug = AutoSlugField(populate_from='name')
    categories = models.ManyToManyField(Category)
    screenshot = models.ImageField(upload_to='screenshot')
    movie_type = models.ForeignKey(MovieType, on_delete=models.PROTECT)
    description = models.TextField()

    def __str__(self):
        return self.name
