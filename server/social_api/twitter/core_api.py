from social_api.util import makeGetApiCall, displayApiCallData, setRequestParams, makePostApiCall

class TwitterCoreApi:
    def __init__(self, bearer_token, debug):
        self.bearer_token = bearer_token
        self.debug = debug

        self.base_url = self.create_base_url()
        self.headers = self.create_headers()


    def create_base_url(self):
        base_url = "https://api.twitter.com/"
        version = "2"
        return base_url + version

    def create_headers(bearer_token):
        headers = {"Authorization": "Bearer {}".format(bearer_token)}
        return headers
