from django.db import models
from django.urls import reverse_lazy


class Link(models.Model):
    """Model for keeping pair of original-shorted links"""
    original = models.URLField(verbose_name="Исходная ссылка")
    shorted_link_code = models.CharField(max_length=255, unique=True, verbose_name="Код сокращенной ссылки")
    secret_key = models.CharField(max_length=455, unique=True, verbose_name="Секретный ключ")
    qr = models.ImageField(upload_to="qr/%Y/%m/%d", blank=True, null=True, verbose_name="QR Код")

    def get_absolute_url(self):
        return reverse_lazy('short_link_redirect', args=[self.shorted_link_code])