from datetime import datetime
from django.test import TestCase
from django.core.urlresolvers import reverse
from rest_framework.test import APIClient
from rest_framework import status

from eav.models import Attribute

from insurances.models import Risk, RiskType 

class ViewTestCase(TestCase):
    """Test suite for the api views."""

    def setUp(self):
        """Define the test client and other test variables."""
        self.client = APIClient()

        # A client creates two new attributes for a new risk type
        self.attribute1_data = {"name": "House Build Year", "datatype": "int"}
        self.attribute2_data = {"name": "House Address", "datatype": "text"}

        self.response_attribute1 = self.client.post(
            '/api/eav_attributes/',
            self.attribute1_data,
            format="json")

        self.response_attribute2 = self.client.post(
            '/api/eav_attributes/',
            self.attribute2_data,
            format="json")

        # A new risk type with two attributes is created
        self.risk_type_data = {
            "name": "Houses",
            "attributes": [
                int(self.response_attribute1.data['id']),
                int(self.response_attribute2.data['id'])
            ]
        }

        self.response_risk_type = self.client.post(
            '/api/risks_types/',
            self.risk_type_data,
            format="json")

        # A new risk instance is created
        self.risk_data1 = {
            "name": "Playboy Maison",
            "type":int(self.response_attribute1.data['id']),
            "attributes":[
                {"attribute_type":self.response_attribute1.data['id'],"value":"1957"}, # House build year (int)
                {"attribute_type":self.response_attribute2.data['id'],"value":"Playboy Street"} # House address (string)
            ]
        }

        self.response_risk1 = self.client.post(
            '/api/risks/',
            self.risk_data1,
            format="json")

        
        # Another new risk instance with wrong data is created for test attributes data types validations
        self.risk_data2 = {
            "name": "Kardashian Maison",
            "type":int(self.response_attribute1.data['id']),
            "attributes":[
                {"attribute_type":self.response_attribute1.data['id'],"value":"String instead of int"}, # House build year (int)
                {"attribute_type":self.response_attribute2.data['id'],"value":"Some street on Malibu"} # House address (string)
            ]
        }

        self.response_risk2 = self.client.post(
            '/api/risks/',
            self.risk_data2,
            format="json")

    def test_api_can_create_attribute(self):
        """Test the api has creation capability."""
        self.assertEqual(self.response_attribute2.status_code, status.HTTP_201_CREATED)

    def test_api_can_create_risk_type(self):
        """Test the api has creation capability."""
        self.assertEqual(self.response_risk_type.status_code, status.HTTP_201_CREATED)

    def test_api_can_create_risk(self):
        """Test the api has creation capability."""
        self.assertEqual(self.response_risk1.status_code, status.HTTP_201_CREATED)

    def test_api_cant_create_risk_with_wrong_data(self):
        """Test the api has creation capability."""
        self.assertEqual(self.response_risk2.status_code, status.HTTP_400_BAD_REQUEST)