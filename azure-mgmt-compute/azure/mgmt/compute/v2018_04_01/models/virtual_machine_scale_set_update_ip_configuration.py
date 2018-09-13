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

from .sub_resource import SubResource


class VirtualMachineScaleSetUpdateIPConfiguration(SubResource):
    """Describes a virtual machine scale set network profile's IP configuration.

    :param id: Resource Id
    :type id: str
    :param name: The IP configuration name.
    :type name: str
    :param subnet: The subnet.
    :type subnet: ~azure.mgmt.compute.v2018_04_01.models.ApiEntityReference
    :param primary: Specifies the primary IP Configuration in case the network
     interface has more than one IP Configuration.
    :type primary: bool
    :param public_ip_address_configuration: The publicIPAddressConfiguration.
    :type public_ip_address_configuration:
     ~azure.mgmt.compute.v2018_04_01.models.VirtualMachineScaleSetUpdatePublicIPAddressConfiguration
    :param private_ip_address_version: Available from Api-Version 2017-03-30
     onwards, it represents whether the specific ipconfiguration is IPv4 or
     IPv6. Default is taken as IPv4.  Possible values are: 'IPv4' and 'IPv6'.
     Possible values include: 'IPv4', 'IPv6'
    :type private_ip_address_version: str or
     ~azure.mgmt.compute.v2018_04_01.models.IPVersion
    :param application_gateway_backend_address_pools: The application gateway
     backend address pools.
    :type application_gateway_backend_address_pools:
     list[~azure.mgmt.compute.v2018_04_01.models.SubResource]
    :param load_balancer_backend_address_pools: The load balancer backend
     address pools.
    :type load_balancer_backend_address_pools:
     list[~azure.mgmt.compute.v2018_04_01.models.SubResource]
    :param load_balancer_inbound_nat_pools: The load balancer inbound nat
     pools.
    :type load_balancer_inbound_nat_pools:
     list[~azure.mgmt.compute.v2018_04_01.models.SubResource]
    """

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'subnet': {'key': 'properties.subnet', 'type': 'ApiEntityReference'},
        'primary': {'key': 'properties.primary', 'type': 'bool'},
        'public_ip_address_configuration': {'key': 'properties.publicIPAddressConfiguration', 'type': 'VirtualMachineScaleSetUpdatePublicIPAddressConfiguration'},
        'private_ip_address_version': {'key': 'properties.privateIPAddressVersion', 'type': 'str'},
        'application_gateway_backend_address_pools': {'key': 'properties.applicationGatewayBackendAddressPools', 'type': '[SubResource]'},
        'load_balancer_backend_address_pools': {'key': 'properties.loadBalancerBackendAddressPools', 'type': '[SubResource]'},
        'load_balancer_inbound_nat_pools': {'key': 'properties.loadBalancerInboundNatPools', 'type': '[SubResource]'},
    }

    def __init__(self, **kwargs):
        super(VirtualMachineScaleSetUpdateIPConfiguration, self).__init__(**kwargs)
        self.name = kwargs.get('name', None)
        self.subnet = kwargs.get('subnet', None)
        self.primary = kwargs.get('primary', None)
        self.public_ip_address_configuration = kwargs.get('public_ip_address_configuration', None)
        self.private_ip_address_version = kwargs.get('private_ip_address_version', None)
        self.application_gateway_backend_address_pools = kwargs.get('application_gateway_backend_address_pools', None)
        self.load_balancer_backend_address_pools = kwargs.get('load_balancer_backend_address_pools', None)
        self.load_balancer_inbound_nat_pools = kwargs.get('load_balancer_inbound_nat_pools', None)