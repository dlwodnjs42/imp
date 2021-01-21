from decouple import config
import requests
import json

def makeGetApiCall(url, params=None, headers=None, debug=False):
    data = requests.get(url, params=params, headers=headers)

    response = dict()
    response['url'] = url
    response['params'] = params
    response['params_pretty'] = json.dumps(params, indent=4)
    response['json_data'] = json.loads(data.content)
    response['json_data_pretty'] = json.dumps(response['json_data'], indent=4)

    if debug:
        displayApiCallData(response)
    return response

def makePostApiCall(url, params, headers=None, data=None, debug=False)
    data = requests.post(url, params=params, headers=headers, data=data)

    response = dict()
    response['url'] = url
    response['params'] = params
    response['headers'] = headers
    response['json_data'] = json.loads(data.content)

    if debug:
        displayApiCallData(response)
    return response

def makePutApiCall(url, params, data=None):
    data = requests.put(url, params=params, data=data)

    response = dict()
    response['url'] = url
    response['params'] = params
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
    print(f"\nURL: {response['url']} \nEndpoints: {response['params_pretty']} \nData: {response['json_data_pretty']}")

