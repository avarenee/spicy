import os
from django.db import models
from spicy.settings import BASE_DIR
from django.core.validators import RegexValidator

color_validator = RegexValidator(
regex=r'^#([A-Fa-f0-9]{6}|[A-Fa-f0-9]{3})$',
message='Enter a valid hexadecimal color code'
)

class SpiceGallery(models.Model):
    name = models.CharField(max_length=30, unique=True)
    color = models.CharField(max_length=7, validators=[color_validator], null=True)
    image_path = os.path.join(BASE_DIR, 'spicegallery/assets/spicegallery/images')
    image = models.FilePathField(path=image_path, null=True)
    basic_description = models.TextField(default="Scientific name.")
    extended_description = models.TextField(default="History, flavor, and uses of this spice.")

    class Meta:
        ordering = ('name',)

    def __str__(self):
        return self.name

class SpiceMix(models.Model):
    name = models.CharField(max_length=30, unique=True)
    color = models.CharField(max_length=7, validators=[color_validator], null=True)
    origin = models.CharField(max_length=30, default="This spice mix has multiple origins.")
    spices = models.ManyToManyField(SpiceGallery)
    dishes = models.TextField(default="Dishes which the spice mix complements.")

    class Meta:
        ordering = ('name',)

    def __str__(self):
        return self.name
