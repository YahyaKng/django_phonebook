from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

class Phonebook(models.Model):
    

    class Meta:
        db_table = 'phonebook'
        managed = True
        verbose_name = 'Phonebook'
        verbose_name_plural = 'Phonebooks'

    name = models.CharField(max_length=100)
    # phonenumber = models.CharField(max_length=30)
    phonenumber = PhoneNumberField()
    def __str__(self):
        return self.name