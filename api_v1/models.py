from django.db import models


class City(models.Model):
    name = models.CharField(max_length=255)
    country = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Route(models.Model):
    title = models.CharField(max_length=255)

    description = models.TextField()

    duration_days = models.IntegerField()

    price = models.DecimalField(
        max_digits=10,
        decimal_places=2
    )

    city = models.ForeignKey(
        City,
        on_delete=models.CASCADE,
        related_name='routes'
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return self.title


class Review(models.Model):
    route = models.ForeignKey(
        Route,
        on_delete=models.CASCADE,
        related_name='reviews'
    )

    username = models.CharField(max_length=255)

    rating = models.IntegerField()

    comment = models.TextField()

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return self.username