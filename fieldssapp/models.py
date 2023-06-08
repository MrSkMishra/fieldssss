from django.db import models

class User(models.Model):
    name = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    age = models.IntegerField()
    experience = models.CharField(max_length=255)
    qualification = models.CharField(max_length=255)

    def __str__(self):
        return self.name

    

class Company(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='companies')
    company_name = models.CharField(max_length=255)
    from_date = models.CharField(max_length=20)
    to_date = models.CharField(max_length=20)

    def __str__(self):
        return f'User : {self.user} , {self.company_name}'
