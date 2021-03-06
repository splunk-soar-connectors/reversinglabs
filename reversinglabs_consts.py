# File: reversinglabs_consts.py
#
# Copyright (c) 2014-2022 Splunk Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software distributed under
# the License is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND,
# either express or implied. See the License for the specific language governing permissions
# and limitations under the License.
#
#
# Status/Progress Messages
REVERSINGLABS_MSG_GOT_RESP = "Got Response from ReversingLabs"
REVERSINGLABS_SUCC_MSG_OBJECT_QUERIED = "ReversingLabs query for {object_name} '{object_value}' finished"
REVERSINGLABS_ERR_MSG_OBJECT_QUERIED = "ReversingLabs query for {object_name} '{object_value}' failed"
REVERSINGLABS_MSG_CONNECTING_WITH_URL = "Querying ReversingLabs using url: '{url}' for hash type: '{hash_type}'"
REVERSINGLABS_SUCC_CONNECTIVITY_TEST = "Test connectivity passed"
REVERSINGLABS_ERR_CONNECTIVITY_TEST = "Test connectivity failed"
REVERSINGLABS_MSG_CHECK_CREDENTIALS = "Please check your credentials or the network connectivity"
REVERSINGLABS_ERR_INVALID_HASH = "Invalid hash"
REVERSINGLABS_ERR_MALWARE_PRESENCE_QUERY_FAILED = "Query to check if hash is malware failed with HTTP return code {ret_code}"
REVERSINGLABS_GENERATED_RANDOM_HASH = "Generated random hash for testing connectivity"

# Jsons used in params, result, summary etc.
REVERSINGLABS_JSON_DETECTIONS = "detections"
REVERSINGLABS_JSON_FOUND = "found"
REVERSINGLABS_JSON_POSITIVES = "positives"
REVERSINGLABS_JSON_TOTAL_SCANS = "total_scans"
REVERSINGLABS_JSON_TOTAL_POSITIVES = "total_positives"
REVERSINGLABS_JSON_STATUS = "status"

# Other constants used in the connector
MAL_PRESENCE_API_URL = 'https://ticloud01.reversinglabs.com/api/databrowser/malware_presence/bulk_query/json'
XREF_API_URL = 'https://ticloud01.reversinglabs.com/api/xref/v2/bulk_query/json'
