from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=100)
    quantity = models.PositiveIntegerField()
    code = models.CharField(max_length=50)
    materials = models.ManyToManyField('RawMaterial', through='ProductMaterial', related_name='products')

    def __str__(self):
        return self.name


class RawMaterial(models.Model):
    name = models.CharField(max_length=255)
    warehouses = models.ManyToManyField('Warehouse', through='WarehouseQuantity')

    def __str__(self):
        return self.name


class ProductMaterial(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    raw_material = models.ForeignKey(RawMaterial, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.product.name} - {self.raw_material.name}"


class Warehouse(models.Model):
    name = models.CharField(max_length=255)
    quantities = models.ManyToManyField('RawMaterial', through='WarehouseQuantity')

    def __str__(self):
        return self.name


class WarehouseQuantity(models.Model):
    warehouse = models.ForeignKey(Warehouse, on_delete=models.CASCADE)
    raw_material = models.ForeignKey(RawMaterial, on_delete=models.CASCADE)
    remainder = models.PositiveIntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.warehouse.name} - {self.raw_material.name}"
