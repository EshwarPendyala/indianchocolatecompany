from django.db import models
from django.urls import reverse
import uuid

class Company(models.Model):
    """Model representing a manufacturer."""
    name = models.CharField(max_length=100,help_text="Enter a company name.")
    estb = models.DateField(auto_now=False, auto_now_add=False,help_text="Enter date of establishment.")
    company_id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    
    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        """Returns the URL to access a particular company instance."""
        return reverse('company-detail', args=[str(self.id)])
    
class Nutrients(models.Model):
    """Model representing a nutrients in gram."""
    nutrient_set_id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    calories = models.IntegerField(help_text="Enter calories amount.")
    protein = models.IntegerField(help_text="Enter protein amount.")
    fibre = models.IntegerField(help_text="Enter fibre amount.")
    fat = models.IntegerField(help_text="Enter fat amount.")
    sugar = models.IntegerField(help_text="Enter sugar amount.")
    carbohydrates = models.IntegerField(help_text="Enter carbohydrates amount.")

class Chocolate(models.Model):
    """Model representing chocolate."""
    chocolate_id = models.UUIDField(primary_key=True, default=uuid.uuid4, help_text='Unique ID for this particular chocolate.')
    name = models.CharField(max_length=100,help_text="Enter chocolate name.")
    manufacturer = models.ForeignKey("Company", on_delete=models.CASCADE)
    price = models.IntegerField(help_text="Enter Price.")
    chocolate_type = models.CharField(help_text="Enter type of chocolate.",max_length=50)
    decription = models.TextField()
    manufacturing_date = models.DateField(auto_now=False, auto_now_add=False)
    expiry_date = models.DateField(auto_now=False, auto_now_add=False)
    nutrients = models.ForeignKey("Nutrients", on_delete=models.CASCADE)
    
    def __str__(self):
        return self.name
    

    