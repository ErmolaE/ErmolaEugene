from django.db import models
#from django.db.models import Q

# class ProductManager(models.Manager):
#     use_for_related_fields = True
 
#     def search(self, query=None):
#         qs = self.get_queryset()
#         if query:
#             or_lookup = (Q(title__icontains=query) | Q(content__icontains=query))
#             qs = qs.filter(or_lookup)
 
#         return qs

class Product(models.Model):

    economic_stages = [("c", "concept"), ("r", "r&d"), ("f", "finished product")]

    id_product = models.IntegerField(primary_key=True)
    product_name = models.CharField(max_length=50)
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to='upload', blank=True, default='app/img/not_avalaible.png')
    matrix_type = models.CharField(max_length=50)
    ligand = models.CharField(max_length=50, blank=True)
    economic_stage = models.CharField(max_length=1, choices=economic_stages)
    registration = models.CharField(max_length=50, blank=True)
    price = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)
    #objects = ProductManager()

    def __str__(self) -> str:
        return self.product_name

class Application(models.Model):

    product = models.ForeignKey('Product', on_delete=models.CASCADE)
    
    immunology = models.BooleanField()
    surgery = models.BooleanField()
    allergology = models.BooleanField()
    infectology = models.BooleanField()
    intensive_therapy = models.BooleanField()
    cardiology = models.BooleanField()

    def __str__(self) -> str:
        return self.product.product_name

# class ConsumerManager(models.Manager):
#     use_for_related_fields = True
 
#     def search(self, query=None):
#         qs = self.get_queryset()
#         if query:
#             or_lookup = (Q(title__icontains=query) | Q(content__icontains=query))
#             qs = qs.filter(or_lookup)
 
#         return qs

class Consumer(models.Model):

    transportations = [("a", "auto"), ("r", "railway"), ("f", "air")]

    consumer_id = models.AutoField(primary_key=True)
    consumer_name = models.CharField(max_length=100)
    adress = models.CharField(max_length=200, blank=True)
    phone_number = models.IntegerField()
    postcode = models.IntegerField(blank=True, null=True)
    site = models.URLField(max_length=100, blank=True)
    transportation = models.CharField(max_length=1, choices=transportations)
    #objects = ConsumerManager()

    def __str__(self) -> str:
        return self.consumer_name

class Consumption(models.Model):

    product = models.ForeignKey('Product', on_delete=models.CASCADE)

    consumer = models.ForeignKey('Consumer', on_delete=models.CASCADE)

    aac = models.IntegerField()

    def __str__(self) -> str:
        return f"{self.product.product_name}, {self.consumer.consumer_name}"

# class SupplierManager(models.Manager):
#     use_for_related_fields = True
 
#     def search(self, query=None):
#         qs = self.get_queryset()
#         if query:
#             or_lookup = (Q(title__icontains=query) | Q(content__icontains=query))
#             qs = qs.filter(or_lookup)
 
#         return qs

class Supplier(models.Model):

    supplier_id = models.AutoField(primary_key=True)
    supplier_name = models.CharField(max_length=100)
    adress = models.CharField(max_length=200, blank=True)
    phone_number = models.IntegerField()
    postcode = models.IntegerField(blank=True, null=True)
    site = models.URLField(max_length=100, blank=True)
    #objects = SupplierManager()

    def __str__(self) -> str:
        return self.supplier_name

# class MaterialManager(models.Manager):
#     use_for_related_fields = True
 
#     def search(self, query=None):
#         qs = self.get_queryset()
#         if query:
#             or_lookup = (Q(title__icontains=query) | Q(content__icontains=query))
#             qs = qs.filter(or_lookup)
 
#         return qs

class Material(models.Model):

    material_id = models.AutoField(primary_key=True)
    material_name = models.CharField(max_length=50)
    molar_mass = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    density = models.DecimalField(max_digits=4, decimal_places=2, blank=True, null=True)
    measure = models.CharField(max_length=10, default="г")
    price = models.DecimalField(max_digits=8, decimal_places=2)
    #objects = MaterialManager()

    supplier = models.ForeignKey('Supplier', on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.material_name
    
class Material_costs_1000units(models.Model):

    product = models.ForeignKey('Product', on_delete=models.CASCADE)

    material = models.ForeignKey('Material', on_delete=models.CASCADE)

    mass_count = models.DecimalField(max_digits=20, decimal_places=2)

    def __str__(self) -> str:
        return f"{self.product.product_name}, {self.material.material_name}"

    def recipe(self, id_product, count):
        res={}
        if self.material.id_product == id_product:
            for m in self.material:
                res[self.material.name]=self.mass_count*count/1000
        return res

class Employee(models.Model):

    employee_id = models.AutoField(primary_key=True)
    full_name = models.CharField(max_length=50)
    position = models.CharField(max_length=50)
    dob = models.DateField()
    rate = models.DecimalField(max_digits=3, decimal_places=2, default=1)

    def __str__(self) -> str:
        return self.full_name