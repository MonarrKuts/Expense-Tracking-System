from django.db import models
from django.contrib.auth.models import User

class UserSpendingCategory(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_spending_category')
    name = models.CharField(max_length=100)
#   Allows users to personalize their expense tracking.
#   Enables categorization and analysis of spending habits.
    
class Expense(models.Model):
    expense_id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    description = models.CharField(max_length=100)
    amount = models.DecimalField(max_digits=10, decimal_places=2)


   
    def __str__(self):
        return self.name
    

#   Expense and Budget models are linked to 
#    UserSpendingCategory for categorized tracking and budgeting.
    



class Budget(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_budget')
    category = models.CharField(max_length=100)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    start_date = models.DateField()
    end_date = models.DateField()
#   Enables users to set planned spending limits for categories or periods.


class Reports(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_reports')
    title = models.CharField(max_length=100)
    description = models.TextField()
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='created_reports')
    created_at = models.DateTimeField(auto_now_add=True)
    

    def __str__(self):
        return self.title

