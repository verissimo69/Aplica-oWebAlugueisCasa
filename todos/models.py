from django.db import models
from django.utils.timezone import now


# Create your models here.
# cadastro cliente
class Client(models.Model):
    nome = models.CharField(max_length=100)
    email =models.EmailField( max_length=254)
    phone = models.CharField(max_length=200)

    def __str__(self):
        return "{} - {}".format(self.nome,self.email)


    class Meta:
        verbose_name = 'Cliente'
        verbose_name_plural ='Clientes'
        ordering =['-id']

# Opções de Imóveis
## Opções de Imóveis
class TypeImmobile(models.TextChoices):
    APARTMENT = 'APARTAMENTO','APARTAMENTO'
    KITNET = 'KITNET','KITNET'
    HOUSE = 'CASA','CASA'

## Cadastro de Imóveis
class Immobile(models.Model):
    code = models.CharField(max_length=100)
    type_item = models.CharField(max_length=100, choices=TypeImmobile.choices)
    address = models.TextField()
    price = models.DecimalField(max_digits=10,decimal_places=2)
    is_locate = models.BooleanField(default=False)
    
    
    def __str__(self):
        return "{} - {}".format(self.code, self.type_item)
    
    class Meta:
        verbose_name = 'Imóvel'
        verbose_name_plural = 'Imóveis'
        ordering = ['-id']

## Cadastrar as Imagens do Imóvel
class ImmobileImage(models.Model):
    image = models.ImageField('Images',upload_to='images')
    immobile = models.ForeignKey(Immobile, related_name='immobile_images', on_delete=models.CASCADE)
    
    def __str__(self):
        return self.immobile.type_item
    

## Registrar Locação
class RegisterLocation(models.Model):
    immobile = models.ForeignKey(Immobile, on_delete=models.CASCADE, related_name='reg_location')
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    dt_start = models.DateTimeField('Inicio')
    dt_end = models.DateTimeField('Fim')
    create_at = models.DateField(default= now, blank=True)
    
    def __str__(self):
        return "{} - {}".format(self.client, self.immobile)
    
    class Meta:
        verbose_name = 'Registrar Locação'
        verbose_name_plural = 'Registrar Locação'
        ordering = ['-id']

