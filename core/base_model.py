from django.db import models


class BaseModel(models.Model):
    """Clase Abstracta BaseModel para heredar en otros modelos.

    fields:
        title (CharField): Título del modelo, máximo 120 caracteres.
        description (TextField): Descripción del modelo, máximo 255 caracteres.
        active (BooleanField): Indica si el registro está activo, por defecto True.
        created_at (DateTimeField): Fecha y hora de creación del registro.
        updated_at (DateTimeField): Fecha y hora de la última actualización del registro.
    """

    title = models.CharField(max_length=120)
    description = models.TextField(max_length=255, blank=True)
    active = models.BooleanField(default=True, blank=True)

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True
        ordering = ["-created"]
        indexes = [
            models.Index(
                fields=["-created"], name="%(app_label)s_%(model_name)s_created_idx"
            ),
        ]
