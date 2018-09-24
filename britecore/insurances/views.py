# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.contenttypes.models import ContentType
from django.shortcuts import render

# Create your views here.
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import generics
from rest_framework import viewsets
from rest_framework import status

from eav.models import Attribute, Value

from .serializers import RiskSerializer, RiskTypeSerializer, EAVAttributeSerializer
from .models import Risk, RiskType

class RiskViewSet(viewsets.ModelViewSet):
    queryset = Risk.objects.all()
    serializer_class = RiskSerializer

    def create(self, request, *args, **kwargs):
        attr_value_list = []
        risk_id = 0
        try:
            risk_create_response = super(RiskViewSet, self).create(request, *args, **kwargs)
            risk_id = int(risk_create_response.data["id"])
            if "attributes" in request.data:
                for attribute in request.data["attributes"]:
                    risk_attribute_value = Value()
                    risk_attribute_value.attribute = Attribute.objects.get(id=int(attribute["attribute_type"]))
                    risk_attribute_value.entity_ct = ContentType.objects.get(app_label="insurances", model="risk")
                    risk_attribute_value.entity_id = int(risk_create_response.data["id"])
                    risk_attribute_value.value = attribute["value"]
                    risk_attribute_value.save()
                    attr_value_list.append(risk_attribute_value)
            return risk_create_response
        except:
            for attr_value in attr_value_list:
                attr_value.delete()
            Risk.objects.get(id=risk_id).delete()
            return Response(status=status.HTTP_400_BAD_REQUEST)

class RiskTypeViewSet(viewsets.ModelViewSet):
    queryset = RiskType.objects.all()
    serializer_class = RiskTypeSerializer

class EAVAttributeViewSet(viewsets.ModelViewSet):
    queryset = Attribute.objects.all()
    serializer_class = EAVAttributeSerializer
