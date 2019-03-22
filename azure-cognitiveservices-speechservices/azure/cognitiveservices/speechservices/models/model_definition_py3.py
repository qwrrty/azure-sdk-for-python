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


class ModelDefinition(Model):
    """ModelDefinition.

    All required parameters must be populated in order to send to Azure.

    :param text: The text used to adapt this language model
    :type text: str
    :param base_model: The base model used for adaptation
    :type base_model:
     ~azure.cognitiveservices.speechservices.models.ModelIdentity
    :param datasets: Datasets used for adaptation
    :type datasets:
     list[~azure.cognitiveservices.speechservices.models.DatasetIdentity]
    :param model_kind: Required. The kind of this model (e.g. acoustic,
     language ...). Possible values include: 'Acoustic', 'AcousticAndLanguage',
     'Language', 'None', 'CustomVoice', 'LanguageGeneration', 'Sentiment',
     'LanguageIdentification'
    :type model_kind: str or
     ~azure.cognitiveservices.speechservices.models.enum
    :param name: Required. The name of the object
    :type name: str
    :param description: The description of the object
    :type description: str
    :param properties: The custom properties of this entity
    :type properties: dict[str, str]
    :param locale: The locale of the contained data
    :type locale: str
    """

    _validation = {
        'model_kind': {'required': True},
        'name': {'required': True},
    }

    _attribute_map = {
        'text': {'key': 'text', 'type': 'str'},
        'base_model': {'key': 'baseModel', 'type': 'ModelIdentity'},
        'datasets': {'key': 'datasets', 'type': '[DatasetIdentity]'},
        'model_kind': {'key': 'modelKind', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'description': {'key': 'description', 'type': 'str'},
        'properties': {'key': 'properties', 'type': '{str}'},
        'locale': {'key': 'locale', 'type': 'str'},
    }

    def __init__(self, *, model_kind, name: str, text: str=None, base_model=None, datasets=None, description: str=None, properties=None, locale: str=None, **kwargs) -> None:
        super(ModelDefinition, self).__init__(**kwargs)
        self.text = text
        self.base_model = base_model
        self.datasets = datasets
        self.model_kind = model_kind
        self.name = name
        self.description = description
        self.properties = properties
        self.locale = locale