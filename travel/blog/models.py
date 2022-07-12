from django.db import models

# Create your models here.

class Destinations(models.Model):
    name = models.CharField(verbose_name="Yonalish nomi*" , blank=True , max_length=60)
    text = models.TextField(verbose_name="Yonalish haqida*" , max_length=2500 , default="text yoq" , blank=True)
    image = models.ImageField(upload_to="images" , verbose_name="Rasm*")
    price = models.PositiveIntegerField(verbose_name="Yonalish narxi*" , default=100)
    price_usd = models.PositiveIntegerField(verbose_name="Yonalish narxi*" , default=100)
    leave = models.DateField(verbose_name="Ketish sanasi " , blank=True)
    back_to = models.DateField(verbose_name="Qaytish sannasi", blank=True)
    

    def __str__(self):
        return str(self.name)
    class Meta:
        verbose_name = "Yonalish"
        verbose_name_plural = "Yonalishlar"
