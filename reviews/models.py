from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from movies.models import Movie

class Review(models.Model):
    movie = models.ForeignKey(
        Movie,
        on_delete=models.PROTECT,
        related_name= 'reviews',
        )
    stars = models.IntegerField(
        validators= [
            MinValueValidator(
                limit_value=0, 
                message='A avaliação não pode ser inferior a 0 estrelas.'),
            MaxValueValidator(
                limit_value=5,
                message='A avaliação não pode ser superior a 5 estrelas.',
            )
        ]
    )
    comment = models.TextField(
        blank=True,
        null=True,
        max_length=500,
    )

    def __str__(self):
        return f'{self.movie}_review'