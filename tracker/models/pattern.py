from django.db import models

class Pattern(models.Model):
    design_house =
    purchase_source =
    purchased_date = models.DateTimeField()
    purchase_url =
    purchase_price =
    printed = bool
    printed_date =
    garment_type =
    fabric_weave =
    fabric_weight =

class Garment(models.Model):
    garment_type = 
