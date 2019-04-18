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


class MongoIndexKeys(Model):
    """Cosmos DB Mongo collection resource object.

    :param keys: List of keys for each Mongo collection in the Azure Cosmos DB
     service
    :type keys: list[str]
    """

    _attribute_map = {
        'keys': {'key': 'keys', 'type': '[str]'},
    }

    def __init__(self, *, keys=None, **kwargs) -> None:
        super(MongoIndexKeys, self).__init__(**kwargs)
        self.keys = keys
