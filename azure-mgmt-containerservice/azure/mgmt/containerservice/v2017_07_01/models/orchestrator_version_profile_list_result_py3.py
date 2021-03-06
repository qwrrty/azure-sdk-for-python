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


class OrchestratorVersionProfileListResult(Model):
    """The list of versions for supported orchestrators.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    All required parameters must be populated in order to send to Azure.

    :ivar id: Id of the orchestrator version profile list result.
    :vartype id: str
    :ivar name: Name of the orchestrator version profile list result.
    :vartype name: str
    :ivar type: Type of the orchestrator version profile list result.
    :vartype type: str
    :param orchestrators: Required. List of orchestrator version profiles.
    :type orchestrators:
     list[~azure.mgmt.containerservice.v2017_07_01.models.OrchestratorVersionProfile]
    """

    _validation = {
        'id': {'readonly': True},
        'name': {'readonly': True},
        'type': {'readonly': True},
        'orchestrators': {'required': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
        'orchestrators': {'key': 'properties.orchestrators', 'type': '[OrchestratorVersionProfile]'},
    }

    def __init__(self, *, orchestrators, **kwargs) -> None:
        super(OrchestratorVersionProfileListResult, self).__init__(**kwargs)
        self.id = None
        self.name = None
        self.type = None
        self.orchestrators = orchestrators
