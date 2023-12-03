from django.db import models

# Create your models here.
class Ritzypro(models.Model):
    name = models.CharField(max_length=255)
    namescarf = models.CharField(max_length=255)
    price = models.CharField(max_length=255)
    pricesale = models.CharField(max_length=255,null=True)
    material = models.CharField(max_length=255)
    color = models.CharField(max_length=255,null=True)
    ProductDescription = models.TextField()
    Dimensions = models.TextField()
    GarmentCare = models.TextField()
    image = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

class Meta:
        ordering = ['-date_added'] 

class Home(models.Model):
    image = models.TextField()
    image2 = models.TextField(null=True,blank = True)
    name = models.CharField(max_length=255)
    namescarf = models.CharField(max_length=255)
    price = models.CharField(max_length=255)
    pricesale = models.CharField(max_length=255 ,null=True,blank = True)
    soldout = models.CharField(max_length=255,null=True ,blank = True)
    status = models.CharField(max_length=255,null=True,blank = True)   


class Chifon(models.Model):
    image = models.TextField()
    name = models.CharField(max_length=255)
    namescarf = models.CharField(max_length=255)
    price = models.CharField(max_length=255)
    status = models.CharField(max_length=255)   
    pricesale = models.CharField(max_length=255,blank = True)
    material = models.CharField(max_length=255 )
    sold = models.CharField(max_length=255,null=True)
    color = models.CharField(max_length=255)
    ProductDescription = models.TextField()
    Dimensions = models.TextField()
    GarmentCare = models.TextField()

class Woven(models.Model):
    image = models.TextField()
    image2 = models.TextField(null=True)
    namescarf = models.CharField(max_length=255)
    price = models.CharField(max_length=255)
    status = models.CharField(max_length=255,blank=True,null=True)   
    pricesale = models.CharField(max_length=255,blank=True)
    material = models.CharField(max_length=255,null=True)
    color = models.CharField(max_length=255)
    ProductDescription = models.TextField()
    sold = models.CharField(max_length=255 ,blank = True)
    quic = models.CharField(max_length=255,blank = True) 


class Lycra(models.Model): 
    image = models.TextField()
    namescarf = models.CharField(max_length=255)
    price = models.CharField(max_length=255)
    status = models.CharField(max_length=255)   
    material = models.CharField(max_length=255)
    color = models.CharField(max_length=255)
    ProductDescription = models.TextField()

class Linen(models.Model): 
    image = models.TextField()
    image2 = models.TextField()
    namescarf = models.CharField(max_length=255)
    price = models.CharField(max_length=255)
    status = models.CharField(max_length=255)   
    material = models.CharField(max_length=255)
    color = models.CharField(max_length=255)
    ProductDescription = models.TextField()


class All(models.Model):
    image = models.TextField()
    image2 = models.TextField(blank = True)
    name = models.CharField(max_length=255)
    namescarf = models.CharField(max_length=255)
    price = models.CharField(max_length=255)
    pricesale = models.CharField(max_length=255 ,blank = True)
    soldout = models.CharField(max_length=255 ,blank = True)
    status = models.CharField(max_length=255,blank = True) 
    quic = models.CharField(max_length=255,blank = True,null=True) 

class Ctag(models.Model):
    image = models.TextField()
    name = models.CharField(max_length=255)
    link = models.TextField()

    