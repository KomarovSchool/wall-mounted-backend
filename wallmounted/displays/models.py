from django.contrib.postgres.fields import DateTimeRangeField
from django.db import models


class Screen(models.Model):
    id = models.AutoField(primary_key=True)
    code = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.code

class SlideShow(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Slide(models.Model):
    slideshow = models.ForeignKey(SlideShow, related_name="slides", on_delete=models.CASCADE)
    image = models.ImageField(upload_to="slides/")
    order = models.PositiveIntegerField()
    duration = models.PositiveIntegerField(help_text="Duration in seconds")

    class Meta:
        ordering = ['order']

    def __str__(self):
        return f"{self.slideshow.name} - Slide {self.order}"

class ScreenContent(models.Model):
    screen = models.ForeignKey(Screen, related_name="contents", on_delete=models.CASCADE)
    time_range = DateTimeRangeField(null=True, blank=True)
    priority = models.IntegerField(default=0)
    slide_show = models.ForeignKey(SlideShow, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return f"{self.screen.code} - {self.time_range} (Priority: {self.priority})"