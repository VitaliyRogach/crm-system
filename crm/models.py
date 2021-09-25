from django.db import models


class Company(models.Model):
    name = models.CharField(max_length=200)
    city = models.CharField(max_length=200)
    street = models.CharField(max_length=200)
    postal_code = models.CharField(max_length=200)
    number = models.CharField(max_length=200)

    def __str__(self):
        return '%s, %s, %s, %s, %s' % (self.name, self.city,
                                       self.street, self.postal_code,
                                       self.number)


class Voucher(models.Model):
    company_name = models.CharField(max_length=255)
    name_of_voucher = models.CharField(max_length=255)
    count_of_days = models.IntegerField(default=18)
    count_of_person = models.IntegerField()
    number = models.CharField(max_length=20)

    def __str__(self):
        return '%s, %s, %s, %s, %s' % (self.company_name, self.name_of_voucher,
                                       self.count_of_days, self.count_of_person,
                                       self.number)
