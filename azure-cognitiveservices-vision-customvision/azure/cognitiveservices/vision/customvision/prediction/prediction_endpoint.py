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

from msrest.service_client import SDKClient
from msrest import Configuration, Serializer, Deserializer
from .version import VERSION
from msrest.pipeline import ClientRawResponse
from msrest.exceptions import HttpOperationError
from . import models


class PredictionEndpointConfiguration(Configuration):
    """Configuration for PredictionEndpoint
    Note that all parameters used to create this instance are saved as instance
    attributes.

    :param api_key:
    :type api_key: str
    :param str base_url: Service URL
    """

    def __init__(
            self, api_key, base_url=None):

        if api_key is None:
            raise ValueError("Parameter 'api_key' must not be None.")
        if not base_url:
            base_url = 'https://southcentralus.api.cognitive.microsoft.com/customvision/v2.0/Prediction'

        super(PredictionEndpointConfiguration, self).__init__(base_url)

        self.add_user_agent('azure-cognitiveservices-vision-customvision/{}'.format(VERSION))

        self.api_key = api_key


class PredictionEndpoint(SDKClient):
    """PredictionEndpoint

    :ivar config: Configuration for client.
    :vartype config: PredictionEndpointConfiguration

    :param api_key:
    :type api_key: str
    :param str base_url: Service URL
    """

    def __init__(
            self, api_key, base_url=None):

        self.config = PredictionEndpointConfiguration(api_key, base_url)
        super(PredictionEndpoint, self).__init__(None, self.config)

        client_models = {k: v for k, v in models.__dict__.items() if isinstance(v, type)}
        self.api_version = '2.0'
        self._serialize = Serializer(client_models)
        self._deserialize = Deserializer(client_models)


    def predict_image_url(
            self, project_id, iteration_id=None, application=None, url=None, custom_headers=None, raw=False, **operation_config):
        """Predict an image url and saves the result.

        :param project_id: The project id
        :type project_id: str
        :param iteration_id: Optional. Specifies the id of a particular
         iteration to evaluate against.
         The default iteration for the project will be used when not specified
        :type iteration_id: str
        :param application: Optional. Specifies the name of application using
         the endpoint
        :type application: str
        :param url:
        :type url: str
        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: ImagePrediction or ClientRawResponse if raw=true
        :rtype:
         ~azure.cognitiveservices.vision.customvision.prediction.models.ImagePrediction
         or ~msrest.pipeline.ClientRawResponse
        :raises:
         :class:`HttpOperationError<msrest.exceptions.HttpOperationError>`
        """
        image_url = models.ImageUrl(url=url)

        # Construct URL
        url = self.predict_image_url.metadata['url']
        path_format_arguments = {
            'projectId': self._serialize.url("project_id", project_id, 'str')
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}
        if iteration_id is not None:
            query_parameters['iterationId'] = self._serialize.query("iteration_id", iteration_id, 'str')
        if application is not None:
            query_parameters['application'] = self._serialize.query("application", application, 'str')

        # Construct headers
        header_parameters = {}
        header_parameters['Content-Type'] = 'application/json; charset=utf-8'
        if custom_headers:
            header_parameters.update(custom_headers)
        header_parameters['Prediction-Key'] = self._serialize.header("self.config.api_key", self.config.api_key, 'str')

        # Construct body
        body_content = self._serialize.body(image_url, 'ImageUrl')

        # Construct and send request
        request = self._client.post(url, query_parameters)
        response = self._client.send(
            request, header_parameters, body_content, stream=False, **operation_config)

        if response.status_code not in [200]:
            raise HttpOperationError(self._deserialize, response)

        deserialized = None

        if response.status_code == 200:
            deserialized = self._deserialize('ImagePrediction', response)

        if raw:
            client_raw_response = ClientRawResponse(deserialized, response)
            return client_raw_response

        return deserialized
    predict_image_url.metadata = {'url': '/{projectId}/url'}

    def predict_image(
            self, project_id, image_data, iteration_id=None, application=None, custom_headers=None, raw=False, **operation_config):
        """Predict an image and saves the result.

        :param project_id: The project id
        :type project_id: str
        :param image_data:
        :type image_data: Generator
        :param iteration_id: Optional. Specifies the id of a particular
         iteration to evaluate against.
         The default iteration for the project will be used when not specified
        :type iteration_id: str
        :param application: Optional. Specifies the name of application using
         the endpoint
        :type application: str
        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: ImagePrediction or ClientRawResponse if raw=true
        :rtype:
         ~azure.cognitiveservices.vision.customvision.prediction.models.ImagePrediction
         or ~msrest.pipeline.ClientRawResponse
        :raises:
         :class:`HttpOperationError<msrest.exceptions.HttpOperationError>`
        """
        # Construct URL
        url = self.predict_image.metadata['url']
        path_format_arguments = {
            'projectId': self._serialize.url("project_id", project_id, 'str')
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}
        if iteration_id is not None:
            query_parameters['iterationId'] = self._serialize.query("iteration_id", iteration_id, 'str')
        if application is not None:
            query_parameters['application'] = self._serialize.query("application", application, 'str')

        # Construct headers
        header_parameters = {}
        header_parameters['Content-Type'] = 'multipart/form-data'
        if custom_headers:
            header_parameters.update(custom_headers)
        header_parameters['Prediction-Key'] = self._serialize.header("self.config.api_key", self.config.api_key, 'str')

        # Construct form data
        form_data_content = {
            'imageData': image_data,
        }

        # Construct and send request
        request = self._client.post(url, query_parameters)
        response = self._client.send_formdata(
            request, header_parameters, form_data_content, stream=False, **operation_config)

        if response.status_code not in [200]:
            raise HttpOperationError(self._deserialize, response)

        deserialized = None

        if response.status_code == 200:
            deserialized = self._deserialize('ImagePrediction', response)

        if raw:
            client_raw_response = ClientRawResponse(deserialized, response)
            return client_raw_response

        return deserialized
    predict_image.metadata = {'url': '/{projectId}/image'}

    def predict_image_url_with_no_store(
            self, project_id, iteration_id=None, application=None, url=None, custom_headers=None, raw=False, **operation_config):
        """Predict an image url without saving the result.

        :param project_id: The project id
        :type project_id: str
        :param iteration_id: Optional. Specifies the id of a particular
         iteration to evaluate against.
         The default iteration for the project will be used when not specified
        :type iteration_id: str
        :param application: Optional. Specifies the name of application using
         the endpoint
        :type application: str
        :param url:
        :type url: str
        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: ImagePrediction or ClientRawResponse if raw=true
        :rtype:
         ~azure.cognitiveservices.vision.customvision.prediction.models.ImagePrediction
         or ~msrest.pipeline.ClientRawResponse
        :raises:
         :class:`HttpOperationError<msrest.exceptions.HttpOperationError>`
        """
        image_url = models.ImageUrl(url=url)

        # Construct URL
        url = self.predict_image_url_with_no_store.metadata['url']
        path_format_arguments = {
            'projectId': self._serialize.url("project_id", project_id, 'str')
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}
        if iteration_id is not None:
            query_parameters['iterationId'] = self._serialize.query("iteration_id", iteration_id, 'str')
        if application is not None:
            query_parameters['application'] = self._serialize.query("application", application, 'str')

        # Construct headers
        header_parameters = {}
        header_parameters['Content-Type'] = 'application/json; charset=utf-8'
        if custom_headers:
            header_parameters.update(custom_headers)
        header_parameters['Prediction-Key'] = self._serialize.header("self.config.api_key", self.config.api_key, 'str')

        # Construct body
        body_content = self._serialize.body(image_url, 'ImageUrl')

        # Construct and send request
        request = self._client.post(url, query_parameters)
        response = self._client.send(
            request, header_parameters, body_content, stream=False, **operation_config)

        if response.status_code not in [200]:
            raise HttpOperationError(self._deserialize, response)

        deserialized = None

        if response.status_code == 200:
            deserialized = self._deserialize('ImagePrediction', response)

        if raw:
            client_raw_response = ClientRawResponse(deserialized, response)
            return client_raw_response

        return deserialized
    predict_image_url_with_no_store.metadata = {'url': '/{projectId}/url/nostore'}

    def predict_image_with_no_store(
            self, project_id, image_data, iteration_id=None, application=None, custom_headers=None, raw=False, **operation_config):
        """Predict an image without saving the result.

        :param project_id: The project id
        :type project_id: str
        :param image_data:
        :type image_data: Generator
        :param iteration_id: Optional. Specifies the id of a particular
         iteration to evaluate against.
         The default iteration for the project will be used when not specified
        :type iteration_id: str
        :param application: Optional. Specifies the name of application using
         the endpoint
        :type application: str
        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: ImagePrediction or ClientRawResponse if raw=true
        :rtype:
         ~azure.cognitiveservices.vision.customvision.prediction.models.ImagePrediction
         or ~msrest.pipeline.ClientRawResponse
        :raises:
         :class:`HttpOperationError<msrest.exceptions.HttpOperationError>`
        """
        # Construct URL
        url = self.predict_image_with_no_store.metadata['url']
        path_format_arguments = {
            'projectId': self._serialize.url("project_id", project_id, 'str')
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}
        if iteration_id is not None:
            query_parameters['iterationId'] = self._serialize.query("iteration_id", iteration_id, 'str')
        if application is not None:
            query_parameters['application'] = self._serialize.query("application", application, 'str')

        # Construct headers
        header_parameters = {}
        header_parameters['Content-Type'] = 'multipart/form-data'
        if custom_headers:
            header_parameters.update(custom_headers)
        header_parameters['Prediction-Key'] = self._serialize.header("self.config.api_key", self.config.api_key, 'str')

        # Construct form data
        form_data_content = {
            'imageData': image_data,
        }

        # Construct and send request
        request = self._client.post(url, query_parameters)
        response = self._client.send_formdata(
            request, header_parameters, form_data_content, stream=False, **operation_config)

        if response.status_code not in [200]:
            raise HttpOperationError(self._deserialize, response)

        deserialized = None

        if response.status_code == 200:
            deserialized = self._deserialize('ImagePrediction', response)

        if raw:
            client_raw_response = ClientRawResponse(deserialized, response)
            return client_raw_response

        return deserialized
    predict_image_with_no_store.metadata = {'url': '/{projectId}/image/nostore'}