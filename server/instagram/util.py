from decouple import config
import requests
import json

def makeGetApiCall(url, params, debug=False):
    data = requests.get(url, params)

    response = dict()
    response['url'] = url
    response['endpoint_params'] = params
    response['endpoint_params_pretty'] = json.dumps(params, indent=4)
    response['json_data'] = json.loads(data.content)
    response['json_data_pretty'] = json.dumps(response['json_data'], indent=4)

    if debug:
        displayApiCallData(response)
    return response

def makePostApiCall(url, params, debug=False)
    data = requests.post(url, params)

    response = dict()
    response['url'] = url
    response['json_data'] = json.loads(data.content)
    return response

def makeDeleteApiCall(url, debug=False):
    response = requests.delete(url)
    return response

def setRequestParams(fields=None, token=None):
    endpointParams = {}
    endpointParams['access_token'] = token if token else config('ACCESS_TOKEN')
    if fields:
        endpointParams['fields'] = fields

    return endpointParams

def displayApiCallData(response):
    print(f"\nURL: {response['url']} \nEndpoints: {response['endpoint_params_pretty']} \nData: {response['json_data_pretty']}")

