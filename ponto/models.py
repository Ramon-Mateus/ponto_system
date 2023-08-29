from django.db import models

class Hours(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    start = models.DecimalField()
    end = models.DecimalField()
    total = models.IntegerField()
    data = models.DateField(auto_now_add=True)
    
    def __str__(self):
        return self.total


class User(models.Model):
    name = models.CharField(max_length=200)
    
    def __str__(self):
        return self.name