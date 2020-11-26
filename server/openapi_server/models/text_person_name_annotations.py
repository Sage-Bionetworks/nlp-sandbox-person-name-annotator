# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from openapi_server.models.base_model_ import Model
from openapi_server.models.text_person_name_annotation import TextPersonNameAnnotation
from openapi_server import util

from openapi_server.models.text_person_name_annotation import TextPersonNameAnnotation  # noqa: E501

class TextPersonNameAnnotations(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, text_person_name_annotations=None):  # noqa: E501
        """TextPersonNameAnnotations - a model defined in OpenAPI

        :param text_person_name_annotations: The text_person_name_annotations of this TextPersonNameAnnotations.  # noqa: E501
        :type text_person_name_annotations: List[TextPersonNameAnnotation]
        """
        self.openapi_types = {
            'text_person_name_annotations': List[TextPersonNameAnnotation]
        }

        self.attribute_map = {
            'text_person_name_annotations': 'textPersonNameAnnotations'
        }

        self._text_person_name_annotations = text_person_name_annotations

    @classmethod
    def from_dict(cls, dikt) -> 'TextPersonNameAnnotations':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The TextPersonNameAnnotations of this TextPersonNameAnnotations.  # noqa: E501
        :rtype: TextPersonNameAnnotations
        """
        return util.deserialize_model(dikt, cls)

    @property
    def text_person_name_annotations(self):
        """Gets the text_person_name_annotations of this TextPersonNameAnnotations.

        A list of text person name annotations  # noqa: E501

        :return: The text_person_name_annotations of this TextPersonNameAnnotations.
        :rtype: List[TextPersonNameAnnotation]
        """
        return self._text_person_name_annotations

    @text_person_name_annotations.setter
    def text_person_name_annotations(self, text_person_name_annotations):
        """Sets the text_person_name_annotations of this TextPersonNameAnnotations.

        A list of text person name annotations  # noqa: E501

        :param text_person_name_annotations: The text_person_name_annotations of this TextPersonNameAnnotations.
        :type text_person_name_annotations: List[TextPersonNameAnnotation]
        """

        self._text_person_name_annotations = text_person_name_annotations
