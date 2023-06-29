from django.db import models
from django.utils.timezone import now
from django.contrib.auth.models import User

class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name="Nombre")
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de Creación")
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de Edición")

    class Meta:
        verbose_name = "categoría"
        ordering = ["-created"]

    def __str__(self):
        return self.name

class Post(models.Model):
    title = models.CharField(max_length=200, verbose_name="Título")
    content = models.TextField(verbose_name="Contenido")
    published = models.DateTimeField(default=now, verbose_name="Fecha de Publicación")
    image = models.ImageField(upload_to="blog", null=True, blank=True, verbose_name="Imagen")
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Autor")
    categories = models.ManyToManyField(Category, related_name="get_posts", verbose_name="Categorías")
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de edición")

    class Meta:
        verbose_name = "entrada"
        ordering = ["-created"]

    def __str__(self):
        return self.title
