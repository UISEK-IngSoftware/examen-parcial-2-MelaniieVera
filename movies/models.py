
from django.db import models

class Movie(models.Model):
    title = models.CharField(max_length=200)
    director = models.CharField(max_length=100)
    release_year = models.PositiveIntegerField()
    duration = models.PositiveIntegerField(help_text="Duración en minutos")
    genre = models.CharField(max_length=100)
    synopsis = models.TextField()
    image = models.ImageField(
        upload_to="movies_images",
        null=True,
        blank=True,
        help_text="Sube una imagen de la película"
    )

    def __str__(self):
        return f"{self.title} ({self.release_year})"
