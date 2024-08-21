from django.db import models
from django.db.models import CharField, ImageField, DecimalField, DateField, TextField, SlugField
from django.utils.text import slugify
from django.utils.translation import gettext_lazy as _
from django_ckeditor_5.fields import CKEditor5Field


class ClickTransaction(models.Model):
    """Класс ClickTransaction"""

    PROCESSING = "processing"
    WAITING = "waiting"
    CONFIRMED = "confirmed"
    CANCELED = "canceled"
    ERROR = "error"

    STATUS = (
        (WAITING, WAITING),
        (PROCESSING, PROCESSING),
        (CONFIRMED, CONFIRMED),
        (CANCELED, CANCELED),
        (ERROR, ERROR),
    )
    click_paydoc_id = models.CharField(
        verbose_name=_("Номер платежа в системе CLICK"), max_length=255, blank=True
    )
    amount = models.DecimalField(
        verbose_name=_("Сумма оплаты (в сумах)"),
        max_digits=9,
        decimal_places=2,
        default="0.0",
    )
    action = models.CharField(
        verbose_name=_("Выполняемое действие"), max_length=255, blank=True, null=True
    )
    status = models.CharField(
        verbose_name=_("Статус"), max_length=25, choices=STATUS, default=WAITING
    )
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    extra_data = models.TextField(blank=True, default="")
    message = models.TextField(blank=True, default="")

    def __str__(self):
        return self.click_paydoc_id

    def change_status(self, status: str, message=""):
        """
        Обновляет статус платежа
        """
        self.status = status
        self.message = message
        self.save(update_fields=["status", "message"])




# Create your models here.
class Packages(models.Model):
    name = CharField(max_length=255)
    image = ImageField(upload_to='media/package_images',
                       blank=True,
                       null=True)
    cost = DecimalField(max_digits=10, decimal_places=2)
    description = CKEditor5Field('Text', config_name='extends')
    duration = CharField(max_length=100)
    depart_time = DateField()
    return_time = DateField()
    destination = CharField(max_length=255)
    slug = SlugField(max_length=255)

    def _get_unique_slug(self):
        slug = slugify(self.name)
        unique_slug = slug
        num = 1
        while Packages.objects.filter(slug=unique_slug).exists():
            unique_slug = f'{slug}-{num}'
            num += 1
        return unique_slug

    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        self.slug = self._get_unique_slug()
        if force_update is True:
            self.slug = slugify(self.name)
        return super().save(force_insert, force_update, using, update_fields)

    def __str__(self):
        return self.name


class Contacts(models.Model):
    name = CharField(max_length=255)
    email = CharField(max_length=255)
    subject = CharField(max_length=255)
    message = TextField()

    def __str__(self):
        return self.name


class Booking(models.Model):
    name = CharField(max_length=255)
    packages = models.ForeignKey(Packages, on_delete=models.CASCADE)
    email = models.EmailField(max_length=255)
    phone = CharField(max_length=25)
    additional_info = TextField(null=True, blank=True)

    def __str__(self):
        return self.name