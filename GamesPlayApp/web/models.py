from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models


class Profile(models.Model):
    AGE_MIN_VALUE = 12
    PASSWORD_MAX_LEN = 30
    FIRST_NAME_MAX_LEN = 30
    LAST_NAME_MAX_LEN = 30

    email = models.EmailField()
    age = models.IntegerField(
        validators=(
            MinValueValidator(AGE_MIN_VALUE),
        ),
    )
    password = models.CharField(
        max_length=PASSWORD_MAX_LEN,
    )

    first_name = models.CharField(
        null=True,
        blank=True,
        max_length=FIRST_NAME_MAX_LEN,
    )
    last_name = models.CharField(
        null=True,
        blank=True,
        max_length=LAST_NAME_MAX_LEN,
    )
    profile_picture = models.URLField(
        null=True,
        blank=True,
    )

    @property
    def full_name(self):
        return f'{self.first_name} {self.last_name}'

class Game(models.Model):
    GAME_CATEGORIES = (
        ("Action", "Action"),
        ("Adventure", "Adventure"),
        ("Puzzle", "Puzzle"),
        ("Strategy", "Strategy"),
        ("Sports", "Sports"),
        ("Board/Card Game", "Board/Card Game"),
        ("Other", "Other"),
    )
    TITLE_MAX_LEN = 15
    RATING_MIN_VALUE = 0.1
    RATING_MAX_VALUE = 5
    MAX_LEVEL_MIN_VALUE = 1

    title = models.CharField(
        unique=True,
        max_length=TITLE_MAX_LEN,
    )
    category = models.CharField(
        max_length=max(len(x) for (x, _) in GAME_CATEGORIES),
        choices=GAME_CATEGORIES,
    )
    rating = models.FloatField(
        validators=(
            MinValueValidator(RATING_MIN_VALUE),
            MaxValueValidator(RATING_MAX_VALUE),
        )
    )

    max_level = models.IntegerField(
        blank=True,
        null=True,
        validators=(
            MinValueValidator(MAX_LEVEL_MIN_VALUE),
        )
    )

    image = models.URLField()

    summary = models.TextField(
        null=True,
        blank=True,
    )
