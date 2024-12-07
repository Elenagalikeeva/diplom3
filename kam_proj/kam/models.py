from django.db import models
from django.contrib.auth.models import User




class Kam(models.Model):
    title = models.CharField(max_length=300)
    description = models.CharField(max_length=300)
    image = models.ImageField(upload_to='kam/image/')
    price = models.CharField(max_length=300, blank=True)
    url = models.URLField(blank=True)

    def __str__(self):
        return self.title


class Vosho(models.Model):
    title = models.CharField(max_length=300)
    description = models.CharField(max_length=300)
    image = models.ImageField(upload_to='kam/image/')
    price = models.CharField(max_length=300)

    def __str__(self):
        return self.title


class More(models.Model):
    title = models.CharField(max_length=300)
    description = models.CharField(max_length=300)
    image = models.ImageField(upload_to='kam/image/')
    price = models.CharField(max_length=300)

    def __str__(self):
        return self.title


class Obzor(models.Model):
    title = models.CharField(max_length=300)
    description = models.CharField(max_length=300)
    image = models.ImageField(upload_to='kam/image/')
    price = models.CharField(max_length=300)

    def __str__(self):
        return self.title


class Vse(models.Model):
    title = models.CharField(max_length=300)
    description = models.CharField(max_length=300)
    image = models.ImageField(upload_to='kam/image/')
    price = models.CharField(max_length=300)

    def __str__(self):
        return self.title


class Rev(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=100, verbose_name="Имя")
    description = models.TextField(verbose_name="Комментарий")
    image = models.ImageField(upload_to='kam/image/', blank=True, null=True, verbose_name="Загрузить аватар")
    created_at = models.DateTimeField(auto_now=True, verbose_name='Дата создания')

    def __str__(self):
        if self.user:
            return f"{self.user}"
        if self.name:
            return f"{self.name}"

