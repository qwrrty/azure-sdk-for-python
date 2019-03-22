# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class TranscriptionDefinition(Model):
    """TranscriptionDefinition.

    All required parameters must be populated in order to send to Azure.

    :param recordings_url: Required.
    :type recordings_url: str
    :param models_property:
    :type models_property:
     list[~azure.cognitiveservices.speechservices.models.ModelIdentity]
    :param locale: The locale of the contained data
    :type locale: str
    :param name: Required. The name of the object
    :type name: str
    :param description: The description of the object
    :type description: str
    :param properties: The custom properties of this entity
    :type properties: dict[str, str]
    """

    _validation = {
        'recordings_url': {'required': True},
        'name': {'required': True},
    }

    _attribute_map = {
        'recordings_url': {'key': 'recordingsUrl', 'type': 'str'},
        'models_property': {'key': 'models', 'type': '[ModelIdentity]'},
        'locale': {'key': 'locale', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'description': {'key': 'description', 'type': 'str'},
        'properties': {'key': 'properties', 'type': '{str}'},
    }

    def __init__(self, **kwargs):
        super(TranscriptionDefinition, self).__init__(**kwargs)
        self.recordings_url = kwargs.get('recordings_url', None)
        self.models_property = kwargs.get('models_property', None)
        self.locale = kwargs.get('locale', None)
        self.name = kwargs.get('name', None)
        self.description = kwargs.get('description', None)
        self.properties = kwargs.get('properties', None)