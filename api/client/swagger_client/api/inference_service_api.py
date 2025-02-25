# Copyright 2021 IBM Corporation
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
# coding: utf-8

"""
    MLX API

    MLX API Extension for Kubeflow Pipelines  # noqa: E501

    OpenAPI spec version: 0.1.27-pipeline-namespace
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from swagger_client.api_client import ApiClient


class InferenceServiceApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def create_service(self, body, **kwargs):  # noqa: E501
        """create_service  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.create_service(body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param ApiInferenceservice body: (required)
        :param str namespace:
        :return: ApiInferenceservice
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.create_service_with_http_info(body, **kwargs)  # noqa: E501
        else:
            (data) = self.create_service_with_http_info(body, **kwargs)  # noqa: E501
            return data

    def create_service_with_http_info(self, body, **kwargs):  # noqa: E501
        """create_service  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.create_service_with_http_info(body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param ApiInferenceservice body: (required)
        :param str namespace:
        :return: ApiInferenceservice
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body', 'namespace']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method create_service" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `create_service`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'namespace' in params:
            query_params.append(('namespace', params['namespace']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']
        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/inferenceservices', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ApiInferenceservice',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_inferenceservices(self, id, **kwargs):  # noqa: E501
        """get_inferenceservices  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_inferenceservices(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: (required)
        :param str namespace:
        :return: ApiInferenceservice
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_inferenceservices_with_http_info(id, **kwargs)  # noqa: E501
        else:
            (data) = self.get_inferenceservices_with_http_info(id, **kwargs)  # noqa: E501
            return data

    def get_inferenceservices_with_http_info(self, id, **kwargs):  # noqa: E501
        """get_inferenceservices  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_inferenceservices_with_http_info(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: (required)
        :param str namespace:
        :return: ApiInferenceservice
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['id', 'namespace']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_inferenceservices" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'id' is set
        if ('id' not in params or
                params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `get_inferenceservices`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'id' in params:
            path_params['id'] = params['id']  # noqa: E501

        query_params = []
        if 'namespace' in params:
            query_params.append(('namespace', params['namespace']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/inferenceservices/{id}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ApiInferenceservice',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def list_inferenceservices(self, **kwargs):  # noqa: E501
        """list_inferenceservices  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.list_inferenceservices(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str page_token:
        :param int page_size:
        :param str sort_by: Can be format of \"field_name\", \"field_name asc\" or \"field_name desc\" Ascending by default.
        :param str filter: A string-serialized JSON dictionary with key-value pairs that correspond to the InferenceService's attribute names and their respective values to be filtered for.
        :param str namespace:
        :return: ApiListInferenceservicesResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.list_inferenceservices_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.list_inferenceservices_with_http_info(**kwargs)  # noqa: E501
            return data

    def list_inferenceservices_with_http_info(self, **kwargs):  # noqa: E501
        """list_inferenceservices  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.list_inferenceservices_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str page_token:
        :param int page_size:
        :param str sort_by: Can be format of \"field_name\", \"field_name asc\" or \"field_name desc\" Ascending by default.
        :param str filter: A string-serialized JSON dictionary with key-value pairs that correspond to the InferenceService's attribute names and their respective values to be filtered for.
        :param str namespace:
        :return: ApiListInferenceservicesResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['page_token', 'page_size', 'sort_by', 'filter', 'namespace']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method list_inferenceservices" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'page_token' in params:
            query_params.append(('page_token', params['page_token']))  # noqa: E501
        if 'page_size' in params:
            query_params.append(('page_size', params['page_size']))  # noqa: E501
        if 'sort_by' in params:
            query_params.append(('sort_by', params['sort_by']))  # noqa: E501
        if 'filter' in params:
            query_params.append(('filter', params['filter']))  # noqa: E501
        if 'namespace' in params:
            query_params.append(('namespace', params['namespace']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/inferenceservices', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ApiListInferenceservicesResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def upload_service(self, uploadfile, **kwargs):  # noqa: E501
        """upload_service  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.upload_service(uploadfile, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param file uploadfile: The inference service metadata to upload. Maximum size of 32MB is supported. (required)
        :param str name:
        :param str namespace:
        :return: ApiInferenceservice
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.upload_service_with_http_info(uploadfile, **kwargs)  # noqa: E501
        else:
            (data) = self.upload_service_with_http_info(uploadfile, **kwargs)  # noqa: E501
            return data

    def upload_service_with_http_info(self, uploadfile, **kwargs):  # noqa: E501
        """upload_service  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.upload_service_with_http_info(uploadfile, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param file uploadfile: The inference service metadata to upload. Maximum size of 32MB is supported. (required)
        :param str name:
        :param str namespace:
        :return: ApiInferenceservice
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['uploadfile', 'name', 'namespace']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method upload_service" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'uploadfile' is set
        if ('uploadfile' not in params or
                params['uploadfile'] is None):
            raise ValueError("Missing the required parameter `uploadfile` when calling `upload_service`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'name' in params:
            query_params.append(('name', params['name']))  # noqa: E501
        if 'namespace' in params:
            query_params.append(('namespace', params['namespace']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}
        if 'uploadfile' in params:
            local_var_files['uploadfile'] = params['uploadfile']  # noqa: E501

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['multipart/form-data'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/inferenceservices/upload', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ApiInferenceservice',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
