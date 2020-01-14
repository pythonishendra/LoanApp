from django.db import models
from datetime import datetime    

# Load Model
class Loan(models.Model):
    first_name=models.CharField(max_length=100)
    last_name=models.CharField(max_length=100)
    email=models.EmailField(max_length=100)
    mobile=models.BigIntegerField()
    address=models.TextField()
    approve_status=models.BooleanField(default=False)
    loan_request_date=models.DateTimeField(default=datetime.now)

    def __str__(self):
        return self.first_name
