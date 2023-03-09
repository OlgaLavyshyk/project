from django.db import models

class Product(models.Model):
    articles = models.CharField(max_length=20)
    brand = models.CharField(max_length=50)
    title = models.CharField(max_length=50)

class Input(models.Model):
    article = models.PositiveIntegerField(
        verbose_name="Введите артикул товара"
    )
class FileInput(models.Model):
    articles = models.FileField(verbose_name="Выберете файл для загрузки", upload_to='xlsx/',null= True, blank=True)

