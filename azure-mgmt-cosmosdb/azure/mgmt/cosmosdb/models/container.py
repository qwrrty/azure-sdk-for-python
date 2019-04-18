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

from .resource import Resource


class Container(Resource):
    """An Azure Cosmos DB container.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    All required parameters must be populated in order to send to Azure.

    :ivar id: The unique resource identifier of the database account.
    :vartype id: str
    :ivar name: The name of the database account.
    :vartype name: str
    :ivar type: The type of Azure resource.
    :vartype type: str
    :param location: The location of the resource group to which the resource
     belongs.
    :type location: str
    :param tags:
    :type tags: dict[str, str]
    :param container_id: Required. Name of the Cosmos DB container
    :type container_id: str
    :param indexing_policy: The configuration of the indexing policy. By
     default, the indexing is automatic for all document paths within the
     container
    :type indexing_policy: ~azure.mgmt.cosmosdb.models.IndexingPolicy
    :param partition_key: The configuration of the partition key to be used
     for partitioning data into multiple partitions
    :type partition_key: ~azure.mgmt.cosmosdb.models.ContainerPartitionKey
    :param default_ttl: Default time to live
    :type default_ttl: int
    :param unique_key_policy: The unique key policy configuration for
     specifying uniqueness constraints on documents in the collection in the
     Azure Cosmos DB service.
    :type unique_key_policy: ~azure.mgmt.cosmosdb.models.UniqueKeyPolicy
    :param conflict_resolution_policy: The conflict resolution policy for the
     container.
    :type conflict_resolution_policy:
     ~azure.mgmt.cosmosdb.models.ConflictResolutionPolicy
    :param _rid: A system generated property. A unique identifier.
    :type _rid: str
    :param _ts: A system generated property that denotes the last updated
     timestamp of the resource.
    :type _ts: object
    :param _etag: A system generated property representing the resource etag
     required for optimistic concurrency control.
    :type _etag: str
    """

    _validation = {
        'id': {'readonly': True},
        'name': {'readonly': True},
        'type': {'readonly': True},
        'container_id': {'required': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
        'location': {'key': 'location', 'type': 'str'},
        'tags': {'key': 'tags', 'type': '{str}'},
        'container_id': {'key': 'properties.id', 'type': 'str'},
        'indexing_policy': {'key': 'properties.indexingPolicy', 'type': 'IndexingPolicy'},
        'partition_key': {'key': 'properties.partitionKey', 'type': 'ContainerPartitionKey'},
        'default_ttl': {'key': 'properties.defaultTtl', 'type': 'int'},
        'unique_key_policy': {'key': 'properties.uniqueKeyPolicy', 'type': 'UniqueKeyPolicy'},
        'conflict_resolution_policy': {'key': 'properties.conflictResolutionPolicy', 'type': 'ConflictResolutionPolicy'},
        '_rid': {'key': 'properties._rid', 'type': 'str'},
        '_ts': {'key': 'properties._ts', 'type': 'object'},
        '_etag': {'key': 'properties._etag', 'type': 'str'},
    }

    def __init__(self, **kwargs):
        super(Container, self).__init__(**kwargs)
        self.container_id = kwargs.get('container_id', None)
        self.indexing_policy = kwargs.get('indexing_policy', None)
        self.partition_key = kwargs.get('partition_key', None)
        self.default_ttl = kwargs.get('default_ttl', None)
        self.unique_key_policy = kwargs.get('unique_key_policy', None)
        self.conflict_resolution_policy = kwargs.get('conflict_resolution_policy', None)
        self._rid = kwargs.get('_rid', None)
        self._ts = kwargs.get('_ts', None)
        self._etag = kwargs.get('_etag', None)
