from rest_framework import serializers

from eav.models import Attribute

from .models import RiskType, Risk

class EAVAttributeSerializer(serializers.ModelSerializer):
    """Serializer to map the eav Attribute instance."""

    class Meta:
        """Meta class to map serializer's fields with the model fields."""

        model = Attribute
        fields = ('id', 'name', 'datatype')


class RiskTypeSerializer(serializers.ModelSerializer):
    """Serializer to map the RiskType instance."""
    attributes_details = EAVAttributeSerializer(many=True, read_only=True, source='attributes')

    class Meta:
        """Meta class to map serializer's fields with the model fields."""

        model = RiskType
        fields = ('id', 'name', 'attributes', 'attributes_details')


class RiskSerializer(serializers.ModelSerializer):
    """Serializer to map the Risk instance."""
    attribute_values = serializers.SerializerMethodField()

    class Meta:
        """Meta class to map serializer's fields with the model fields."""

        model = Risk
        fields = '__all__'

    def get_attribute_values(self, obj):
        """"""
        return [{"id": item.id, "name": item.attribute.name, "value": item.value} for item in obj.eav.get_values()]
        