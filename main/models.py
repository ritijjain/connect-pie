from django.db import models
import uuid
import secrets

class University(models.Model):
    name = models.CharField(max_length=200)
    location = models.CharField(max_length=200)
    shortname = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return f'{self.name}'

class uClass(models.Model):
    fall20 = 'Fall 2020'
    spring20 = 'Spring 2021'
    term_choices = [(fall20, 'Fall 2020'), (spring20, 'Spring 2021')]
    
    uni = models.ForeignKey(University, on_delete=models.CASCADE) #Relation
    class_code = models.CharField(max_length=100)
    description = models.CharField(max_length=500)
    term = models.CharField(choices=term_choices, max_length=100, default=fall20)
    instructor = models.CharField(max_length=500)
    uclass_id = models.CharField(max_length=120, default='none')

    def save(self, *args, **kwargs):
        self.uclass_id = self.class_code + str(secrets.token_hex(2))
        super(uClass, self).save(*args, **kwargs)

    def __str__(self):
        return f'{self.class_code}'

class Note(models.Model):
    uClass = models.ForeignKey(uClass, on_delete=models.CASCADE) #Relation
    content = models.TextField()

    def __str__(self):
        return f'{self.uClass.uclass_id} Note'

class URL(models.Model):
    uClass = models.ForeignKey(uClass, on_delete=models.CASCADE) #Relation
    description = models.CharField(max_length=500)
    url = models.URLField(max_length=500)