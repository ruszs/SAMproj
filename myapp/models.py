from django.db import models

class Student(models.Model):
    YEAR_LEVEL_CHOICES = [
        ('1', '1st Year'),
        ('2', '2nd Year'),
        ('3', '3rd Year'),
        ('4', '4th Year'),
    ]

    name = models.CharField(max_length=100)
    address = models.TextField()
    year_level = models.CharField(max_length=1, choices=YEAR_LEVEL_CHOICES)
    program_course = models.CharField(max_length=100)
    email = models.EmailField(unique=True)

    def __str__(self):
        return self.name
