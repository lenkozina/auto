from django.core.validators import RegexValidator
from django.db import models


class Slider(models.Model):
    """Фотки слайдера в шапке"""
    image = models.ImageField(
        verbose_name='Путь до фотки',
        upload_to='img/slider',
        null=True, blank=True
    )
    text = models.TextField(
        max_length=256,
        null=True, blank=True
    )

    def __str__(self):
        return self.image.name

CATEGORIES = (
    ('COMMON', 'ОБЩИЕ ФОТО'),
    ('STAFF', 'ФОТО ПЕРСОНАЛА'),
)

class Gallery(models.Model):
    """Фотки галереи со временем добавления"""
    image = models.ImageField(
        verbose_name='Путь до фотки',
        upload_to='gallery',
        null=True, blank=True
    )
    add_datetime = models.DateTimeField(
        verbose_name='время добавления фото',
        auto_now=True
    )
    text = models.TextField(
        max_length=256,
        null=True, blank=True
    )
    category = models.TextField(
        max_length=256,
        choices=CATEGORIES,
        null=True, blank=True
    )

    def __str__(self):
        return self.image.name


class ServiceCategory(models.Model):
    """Категории услуг"""
    title = models.CharField(
        verbose_name='наименование категории услуг',
        max_length=128,
        null=True, blank=True
    )
    desc = models.TextField(
        verbose_name='зачем нужна эта категория услуг',
        max_length=1200,
        null=True, blank=True
    )
    image = models.ImageField(
        verbose_name='путь до фотки',
        upload_to='img/services',
        null=True, blank=True
    )
    icon = models.CharField(
        verbose_name='наименование иконки',
        max_length=50,
        null=True, blank=True
    )

    def __str__(self):
        return self.title

class Service(models.Model):
    """Услуги"""
    category = models.ForeignKey(
        ServiceCategory,
        on_delete=models.SET_NULL,
        null = True, blank = True
    )
    title = models.CharField(
        verbose_name='наименование услуги',
        max_length=128,
        null=True, blank=True
    )
    desc = models.TextField(
        verbose_name='описание',
        max_length=1200,
        null=True, blank=True
    )
    price = models.PositiveSmallIntegerField(
        verbose_name='цена',
        null=True, blank=True
    )

    def __str__(self):
        return f'{self.category} - {self.title}'

phone_regex = RegexValidator(
        regex=r'^\+?7?\d{10}$',
        message="Номер телефона должен быть в формате +79998887766")

class Feedback(models.Model):
    fio = models.CharField(
        verbose_name='Ваше ФИО',
        max_length=128,
        null=True, blank=True
    )
    phone_number = models.CharField(
        verbose_name='Ваш номер телефона',
        validators=[phone_regex],
        max_length=17,
        blank=True
    )
    text = models.TextField(
        verbose_name='Ваш отзыв',
        max_length=1024,
        null=True, blank=True
    )
    add_datetime = models.DateTimeField(
        verbose_name='время добавления отзыва',
        auto_now=True
    )

    def __str__(self):
        return f'{self.fio}{self.phone_number}'

