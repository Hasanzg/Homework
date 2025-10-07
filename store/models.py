from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from datetime import datetime

class Video(models.Model):
    movie_id = models.IntegerField(
        primary_key=True,
        validators=[
            MinValueValidator(100000),
            MaxValueValidator(999999)
        ])
    movie_title = models.CharField('Title', max_length=200)
    actor1_name = models.CharField('Actor 1', max_length=100, blank=True)
    actor2_name = models.CharField('Actor 2', max_length=100, blank=True)
    director_name = models.CharField('Director', max_length=100, blank=True)

    GENRE_CHOICES = [
        ('COM', 'Comedy'),
        ('ROM', 'Romance'),
        ('ACT', 'Action'),
        ('DRM', 'Drama'),
        ('HOR', 'Horror'),
        ('OTH', 'Other'),
    ]
    movie_genre = models.CharField('Genre', max_length=10, choices=GENRE_CHOICES, default='OTH')
    release_year = models.PositiveIntegerField(
        'Release Year',
        validators=[MinValueValidator(1888), MaxValueValidator(datetime.now().year + 1)]
    )
    DurationMinutes = models.PositiveIntegerField(
        validators=[
            MaxValueValidator(600)
        ]
    )
    Country = models.CharField(max_length=50)
    Rating = models.DecimalField(
        max_digits=4,
        decimal_places=2,
        validators=[MinValueValidator(0), MaxValueValidator(10)]
    )
    '''
    def __str__(self):
        return f"{self.movie_title} ({self.release_year})"
        '''