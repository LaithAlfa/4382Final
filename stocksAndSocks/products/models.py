from django.db import models

class Product(models.Model):
    link = models.TextField()
    title = models.TextField()
    description = models.TextField()
    price = models.DecimalField(decimal_places=2, max_digits=4)

    def __str__(self):
        return self.title[:50]

class Buyer(models.Model):
    fName = models.TextField()
    lName = models.TextField()
    uName = models.TextField()
    email = models.TextField()
    address = models.TextField()
    address2 = models.TextField()
    country = models.TextField()
    state = models.TextField()
    zipCode = models.IntegerField(max_length=5)

    def __str__(self):
        return self.email[:50]

class Payment(models.Model):
    nameOnCard = models.TextField()
    cardNumber = models.IntegerField(max_length=16)
    cardExp = models.TextField(max_length=5)
    cardCVV = models.IntegerField(max_length=3)

    def __str__(self):
        return self.cardNumber[:16]


