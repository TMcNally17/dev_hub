from django.db import models


class Donation(models.Model):
    
    first_name = models.CharField(max_length=150, blank=False, null=False)
    last_name = models.CharField(max_length=150, blank=False, null=False)
    email = models.EmailField(blank=False, null=False)
    donation_amount = models.DecimalField(max_digits=6, decimal_places=2)
    date = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        
        return "{0},{1},{2}".format(self.email, self.donation_amount, self.date)