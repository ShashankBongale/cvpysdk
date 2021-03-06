# -*- coding: utf-8 -*-

# --------------------------------------------------------------------------
# Copyright Commvault Systems, Inc.
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
# --------------------------------------------------------------------------

"""Helper file to maintain all the constants for index server and datacube

IndexServerConstants            -       Maintains constants for index server

"""


class IndexServerConstants:
    """Class to maintain all the index server related constants"""

    ROLE_DATA_ANALYTICS = "Data Analytics"
    ROLE_EXCHANGE_INDEX = "Exchange Index"

    ENGINE_NAME = "engineName"
    CLOUD_ID = "cloudID"
    ROLES = "version"
    HOST_NAME = "hostName"
    CLOUD_NAME = 'internalCloudName'
    CLIENT_NAME = 'clientName'
    CI_SERVER_URL = 'cIServerURL'
    TYPE = 'type'
    BASE_PORT = 'basePort'
    CLIENT_ID = 'clientId'
    SERVER_TYPE = 'serverType'
    INDEX_SERVER_CLIENT_ID = 'indexServerClientId'

    OPERATION_ADD = 1
    OPERATION_DELETE = 2
    OPERATION_EDIT = 3

    REQUEST_JSON = {
        "opType": OPERATION_ADD,
        "type": 1,
        "configureNodes": True,
        "solrCloudInfo": {
            "roles": []
        },
        "cloudNodes": [],
        "cloudInfoEntity": {},
        "cloudMetaInfos": []

    }
