from django.db import models

class Sensor(models.Model):
    name = models.CharField()
    description = models.TextField(max_length=255)


class Measurement(models.Model):
    sensor = models.ForeignKey(Sensor, on_delete=models.CASCADE, related_name='measurements')
    temperature = models.FloatField(max_length=3)
    created_at = models.DateTimeField(auto_now=True)

