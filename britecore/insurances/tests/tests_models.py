# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.test import TestCase

from eav.models import Attribute

from insurances.models import Risk, RiskType

class ModelTestCase(TestCase):
    """ This class define the test suite for Risks models
    """
    def setUp(self):
        """ Define the test client and other test variables.
        """
        # Insurers wants to create some new risk types for both automobile and houses
        self.automobile_risk_type = RiskType(name="automobiles")
        self.automobile_risk_type.save()

        self.house_risk_type = RiskType(name="houses")
        self.house_risk_type.save()

        # Insurers wants to add some properties to automobile risk type
        automobile_year = Attribute.objects.create(name='year', datatype=Attribute.TYPE_INT)
        automobile_kilometers = Attribute.objects.create(name='km', datatype=Attribute.TYPE_FLOAT)
        self.automobile_risk_type.attributes.add(automobile_year)
        self.automobile_risk_type.attributes.add(automobile_kilometers)

        # Insurers wants to add some new risk of type automobile and fill data
        self.risk_vin = Risk(name="Vin Diesel Ferrari", type=self.automobile_risk_type)
        self.risk_vin.eav.year = 2010
        self.risk_vin.eav.km = 25000
        self.risk_vin.save()

        self.risk_elvis = Risk(name="Elvis Presley Cadillac", type=self.automobile_risk_type)
        self.risk_elvis.eav.year = 1959
        self.risk_elvis.eav.km = 370000
        self.risk_elvis.save()

    def test_risk_types_count(self):
        """ Test that we have two risk types.
        """
        self.assertEqual(2, RiskType.objects.count())

    def test_risk_types_attribute_count(self):
        """ Test that automobile risk type just have two attributes.
        """
        self.assertEqual(2, self.automobile_risk_type.attributes.count())
    
    def test_risk_attributes_values(self):
        """ Test that we can filter risks by previous set values
        """
        elvis_car_risk = Risk.objects.get(name='Elvis Presley Cadillac')
        self.assertEqual(elvis_car_risk.eav.year, 1959)