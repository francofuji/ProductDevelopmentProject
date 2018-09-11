from django.db.models.signals import post_save
from django.dispatch import receiver

from insurances.models import Risk

@receiver(post_save, sender=Risk)
def validate_created_risk(sender, instance, created, **kwargs):
    pass