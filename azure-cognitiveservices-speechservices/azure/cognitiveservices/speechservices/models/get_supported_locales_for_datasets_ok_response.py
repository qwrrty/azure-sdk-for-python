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


class GetSupportedLocalesForDatasetsOKResponse(Model):
    """IReadOnlyDictionary`2.

    :param none:
    :type none: list[str]
    :param language:
    :type language: list[str]
    :param acoustic:
    :type acoustic: list[str]
    :param pronunciation:
    :type pronunciation: list[str]
    :param custom_voice:
    :type custom_voice: list[str]
    :param language_generation:
    :type language_generation: list[str]
    """

    _attribute_map = {
        'none': {'key': 'None', 'type': '[str]'},
        'language': {'key': 'Language', 'type': '[str]'},
        'acoustic': {'key': 'Acoustic', 'type': '[str]'},
        'pronunciation': {'key': 'Pronunciation', 'type': '[str]'},
        'custom_voice': {'key': 'CustomVoice', 'type': '[str]'},
        'language_generation': {'key': 'LanguageGeneration', 'type': '[str]'},
    }

    def __init__(self, **kwargs):
        super(GetSupportedLocalesForDatasetsOKResponse, self).__init__(**kwargs)
        self.none = kwargs.get('none', None)
        self.language = kwargs.get('language', None)
        self.acoustic = kwargs.get('acoustic', None)
        self.pronunciation = kwargs.get('pronunciation', None)
        self.custom_voice = kwargs.get('custom_voice', None)
        self.language_generation = kwargs.get('language_generation', None)