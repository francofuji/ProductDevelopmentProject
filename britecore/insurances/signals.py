from django.db.models.signals import post_save
from django.dispatch import receiver

from eav.models import Value

from insurances.models import Risk

@receiver(post_save, sender=Value)
def validate_created_risk(sender, instance, created, **kwargs):
    pass