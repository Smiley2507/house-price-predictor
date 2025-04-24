from django.db import models

# Create your models here.
class PredictionResult(models.Model):
    house_size = models.FloatField()
    predicted_price = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"House {self.id}: {self.house_size} sq ft - ${self.predicted_price:.2f}"