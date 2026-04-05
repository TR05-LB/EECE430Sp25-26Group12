from django.db import models
from django.core.validators import MinValueValidator

class VolleyballPlayer(models.Model):
    POSITION_CHOICES = [
        ('SETTER', 'Setter'),
        ('OUTSIDE', 'Outside Hitter'),
        ('MIDDLE', 'Middle Blocker'),
        ('OPPOSITE', 'Opposite Hitter'),
        ('LIBERO', 'Libero'),
    ]
    
    name = models.CharField(max_length=200)
    date_joined = models.DateField()
    position = models.CharField(max_length=20, choices=POSITION_CHOICES)
    salary = models.DecimalField(
        max_digits=10, 
        decimal_places=2,
        validators=[MinValueValidator(0)]
    )
    contact_person = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['-date_joined']
    
    def __str__(self):
        return f"{self.name} - {self.position}"