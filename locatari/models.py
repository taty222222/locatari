from django.utils import timezone
from django.db import models
from django.contrib.auth.models import User
from decimal import Decimal

class Locatari(models.Model):
    objects = models.Manager()

    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='locatar', null=True, blank=True)
    apartament = models.ForeignKey('Apartament', on_delete=models.CASCADE, null=True,
                                   blank=True)

    def __str__(self):
        return f"Locatar {self.pk} - {self.apartament or 'No apartament'}"

class Meta:
    verbose_name_plural = "Locatari"
    verbose_name = "Locatar"



class Apartament(models.Model):
    objects = models.Manager()

    numar = models.CharField(max_length=10, unique=True)
    scara = models.CharField(null=True, blank=True, max_length=100)
    etaj = models.IntegerField(null=True, blank=True)


    def __str__(self):
        return f"Apartament {self.numar}, Scara {self.scara or 'Unknown'}"

    class Meta:
        verbose_name_plural = "Apartamente"
        verbose_name = "Apartament"



class WaterMeterReading(models.Model):
    apartament = models.ForeignKey(Apartament, on_delete=models.CASCADE)
    date = models.DateField(auto_now_add=True)
    hot_water_index = models.DecimalField(max_digits=10, decimal_places=2)
    cold_water_index = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"Reading for {self.apartament} - {self.date}"


class Index(models.Model):
    value = models.IntegerField()
    date = models.DateField()


class Payment(models.Model):
    objects = models.Manager()

    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    index = models.ForeignKey(Index, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2, default=Decimal('0.00'))
    payment_date = models.DateField()
    is_paid = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.user} - {self.amount} - {self.payment_date}'


class FacturiIntretinere(models.Model):
    objects = models.Manager()

    luna = models.DateField(default=timezone.now)
    pdf_factura = models.FileField(upload_to='locatari/lista_facturi/', default='default.pdf')
    contor_valoare = models.FloatField(default=0.0)
    suma_plata = models.DecimalField(max_digits=10, decimal_places=2, default=Decimal('0.00'))
    data_adaugarii = (models.DateTimeField(default=timezone.now))
    achitata = models.BooleanField(default=False)
    apartment = models.ForeignKey(Apartament, on_delete=models.CASCADE)

    class CustomManager(models.Manager):
        def get_queryset(self):
            return super().get_queryset().filter(achitata=True)

    custom_manager = models.Manager()

    def __str__(self):
        return f"Factura {self.apartment} pentru luna {self.luna}"

    class Meta:
        verbose_name_plural = "Facturi"
        verbose_name = "Factura"





class Aviz(models.Model):
    objects = models.Manager()

    avize = models.TextField(default="Default content")
    titlu = models.CharField(max_length=100)
    continut = models.TextField()
    data_postarii = models.DateTimeField(default=timezone.now)
    eta = models.IntegerField(default=0)

    def __str__(self):
        return self.titlu

    class Meta:
        verbose_name_plural = "Avize"
        verbose_name = "Aviz"


class Reclamatii(models.Model):
    objects = models.Manager()

    CATEGORY_CHOICES = [
        ('maintenance', 'Maintenance'),
        ('noise', 'Noise'),
        ('security', 'Security'),
        ('other', 'Other'),
    ]

    user = models.ForeignKey(User, null=True, on_delete=models.CASCADE)
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES, default='other')
    titlu = models.CharField(max_length=100, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    status = models.CharField(max_length=20)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    def __str__(self):
        return f"{self.user.username} - {self.titlu} - {self.status}"


    class Meta:
        verbose_name_plural = "Reclamatii"
        verbose_name = "Reclamatie"