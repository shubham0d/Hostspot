from django.db import models

# Create your models here.
class DefaultConf(models.Model):
    WHAT_TO_HOST = (
        ('W', 'Website'),
        ('V', 'Video'),
        ('I', 'Image'),
        ('O', 'Other'),
    )
    imageId = models.CharField(max_length=1000, primary_key=True)
    creationDate = models.DateField()
    url = models.CharField(max_length=1000)
    expireDate = models.IntegerField()
    hostingType = models.CharField(max_length=1, choices=WHAT_TO_HOST)
    active = models.BooleanField(default=False)
