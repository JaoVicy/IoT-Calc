from django.db import models

class GeoPoint(models.Model):
    latitude = models.FloatField()
    longitude = models.FloatField()
    distance = models.FloatField(null=True, blank=True)  # Distância até o ponto de referência (opcional)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"({self.latitude}, {self.longitude}) - {self.distance or 'N/A'} km"