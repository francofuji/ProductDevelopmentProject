from django.conf.urls import url, include
from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework import routers, serializers, viewsets

from .views import RiskViewSet, RiskTypeViewSet, EAVAttributeViewSet

router = routers.DefaultRouter()
router.register(r'risks', RiskViewSet)
router.register(r'risks_types', RiskTypeViewSet)
router.register(r'eav_attributes', EAVAttributeViewSet)



urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]