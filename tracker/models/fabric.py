from django.db import models

class Fabric(models.Model):
    fiber = models.ForeignKey()
    color = models.CharField(max_length=200)
    text = models.TextField()
    weave =
    width =
    length =
    textile =
    washed =
    purchased = 
    opacity =
    origin_country =
    purchase_source =
    purchased_date = models.DateTimeField()
    purchase_url =
    purchase_price =
    image =
    weight =
    weight_units =

class Textile(models.Model):
    textile =
    textile_type =

class Color(models.Model):
    color =
    color_family =

class Fiber(models.Model):
    fiber =
    is_natrual =
