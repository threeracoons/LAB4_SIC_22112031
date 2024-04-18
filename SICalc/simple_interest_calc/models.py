from django.db import models

class InterestCalculation(models.Model):
    principal_amount = models.DecimalField(max_digits=10, decimal_places=2)
    interest_rate = models.DecimalField(max_digits=5, decimal_places=2)
    time_period = models.IntegerField()  # Time period in years
