from django.db import models

# company id, description, title, salary, hours
class Listing(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    salary = models.IntegerField()
    hours = models.IntegerField()
    companyid = models.IntegerField()

    def __str__(self):
        return self.name


