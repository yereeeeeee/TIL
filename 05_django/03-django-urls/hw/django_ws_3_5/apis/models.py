from django.db import models
from django.core.validators import URLValidator
from django.core.validators import MinLengthValidator

class APIInfo(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    api_url = models.URLField(max_length=60,
        validators = [
            MinLengthValidator(15)
        ],
    )
    documentation_url = models.URLField()
    auth_required = models.BooleanField()
    additional_info = models.JSONField(blank = True, null = True, default = None)
    created_at = models.DateTimeField(auto_now_add=True)
