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


class IntegrationAccountSessionFilter(Model):
    """The integration account session filter.

    :param changed_time: The changed time of integration account sessions.
    :type changed_time: datetime
    """

    _validation = {
        'changed_time': {'required': True},
    }

    _attribute_map = {
        'changed_time': {'key': 'changedTime', 'type': 'iso-8601'},
    }

    def __init__(self, changed_time):
        self.changed_time = changed_time