from django.db import models
from usermanagement.common.models import BaseModel


class Product(BaseModel):
    web_id = models.CharField(max_length=50, unique=True)
    slug = models.SlugField(max_length=255)
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    is_active = models.BooleanField(default=False)

    class Meta:
        permissions = [('can_add_new_product', 'can add new product'), ('dg_view_product', 'OBP can view product')]
        
    def __str__(self):
        return self.name
