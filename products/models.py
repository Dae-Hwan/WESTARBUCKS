from django.db import models

class Menu(models.Model):
    name = models.CharField(max_length=45)
    
    class Meta():
        db_table = 'menu'

class Categories(models.Model):
    menu = models.ForeignKey(Menu, on_delete=models.CASCADE)
    name = models.CharField(max_length=45)
    
    class Meta():
        db_table = 'categories'

class Products(models.Model):
    categories = models.ForeignKey(Categories, on_delete=models.CASCADE)
    nutritions = models.ForeignKey('Nutritions', on_delete=models.CASCADE, default = '')
    korean_name = models.CharField(max_length=45)
    english_name = models.CharField(max_length=45)
    description = models.TextField(null = True)

    class Meta():
        db_table = 'products'

class Images(models.Model):
    products = models.ForeignKey(Products, on_delete=models.CASCADE)
    image_url = models.CharField(max_length = 2000, default = '')

    class Meta():
        db_table = 'images'
    
class Nutritions(models.Model):
    one_serving_kcal = models.DecimalField(max_digits = 6, decimal_places = 2)
    sodium_mg = models.DecimalField(max_digits = 6, decimal_places = 2)
    saturated_fat_g = models.DecimalField(max_digits = 6, decimal_places = 2)
    sugars_g = models.DecimalField(max_digits = 6, decimal_places = 2)
    protein_g = models.DecimalField(max_digits = 6, decimal_places = 2)
    caffeine_mg = models.DecimalField(max_digits = 6, decimal_places = 2)
    size_ml = models.CharField(max_length=45)
    size_fluid_ounce = models.CharField(max_length=45)

    class Meta():
        db_table = 'nutritions'

class Allergy(models.Model):
    name = models.CharField(max_length = 45)

    class Meta():
        db_table = 'allergy'


class Allergy_drink(models.Model):
    products = models.ForeignKey(Products, on_delete = models.CASCADE)
    allergy = models.ForeignKey(Allergy, on_delete = models.CASCADE)
    
    class Meta():
        db_table = 'allergy_drink'
        


