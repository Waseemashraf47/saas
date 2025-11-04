from django.db import models

# Create your models here.
class PageVisit(models.Model):
    # db table to log page visits
    # id -> automatically added primary key 1,2,3,4.......
    path = models.TextField(blank=True, null=True) # Col
    timestamp = models.DateTimeField(auto_now_add=True) # Col

    # def __str__(self):
    #     return f"Visited {self.path} at {self.timestamp}"
    # 1H23Minutes
