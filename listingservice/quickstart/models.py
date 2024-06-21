from django.db import models

# company id, description, title, salary, hours
class Listing(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=500)
    salary = models.IntegerField()
    hours = models.IntegerField()
    companyid = models.IntegerField()

    class Meta:
        ordering=["created"]