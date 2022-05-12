from django.db import models

class TVShow(models.Model):
    GENRE_CHOICE = (
        ('Detective', 'Detective'),
        ('Comedy', 'Comedy'),
        ('Horror', 'Horror'),
        ('Drama', 'Drama'),
        ('Romantic', 'Romantic'),
        ('Anime', 'Anime')
    )

    title = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='')
    quantity = models.IntegerField()
    genre = models.CharField(choices=GENRE_CHOICE, max_length=100)
    date_filmed = models.DateField()

    def __str__(self):
        return self.title


