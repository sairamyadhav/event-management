from django.db import models

class AbstractBase(models.Model):
    created_on = models.DateTimeField('created on', auto_now_add=True)
    updated_on = models.DateTimeField('updated on', auto_now=True)
    is_deleted = models.BooleanField('is deleted', default=False)

    class Meta:
        abstract = True
