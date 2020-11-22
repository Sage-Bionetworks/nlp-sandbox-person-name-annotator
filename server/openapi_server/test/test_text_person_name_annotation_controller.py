# coding: utf-8

from __future__ import absolute_import
import unittest

from flask import json
from six import BytesIO

from openapi_server.models.error import Error  # noqa: E501
from openapi_server.models.note import Note  # noqa: E501
from openapi_server.models.text_person_name_annotations import TextPersonNameAnnotations  # noqa: E501
from openapi_server.test import BaseTestCase


class TestTextPersonNameAnnotationController(BaseTestCase):
    """TextPersonNameAnnotationController integration test stubs"""

    def test_create_text_person_name_annotations(self):
        """Test case for create_text_person_name_annotations

        Annotate person names in a clinical note
        """
        note = {
  "noteType" : "loinc:LP29684-5",
  "patientId" : "507f1f77bcf86cd799439011",
  "text" : "This is the content of a clinical note."
}
        headers = {
            'Accept': 'application/json',
            'Content-Type': 'application/json',
        }
        response = self.client.open(
            '/api/v1/textPersonNameAnnotations',
            method='POST',
            headers=headers,
            data=json.dumps(note),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    unittest.main()
