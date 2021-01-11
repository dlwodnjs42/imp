from social_api.util import makeGetApiCall, displayApiCallData, setRequestParams, makePostApiCall
from social_api.twitter.core_api import TwitterCoreApi

"""
At our Basic access level, you will be limited to receive 500,000 Tweets per month per project from either the filtered stream or search Tweets endpoints. For example, if you consumed 200,000 Tweets with filtered stream, you will be able to receive an additional 300,000 Tweets from either filtered stream or search Tweets. Once you have used up this allotment, you will need to wait until the next monthly period begins, which is set to the day that your developer account was approved.

https://developer.twitter.com/en/docs/twitter-api/tweets/filtered-stream/api-reference
"""



class FilteredStreamAPI(TwitterCoreApi):

    def updateRules(self, rules, update="add"):
        """
        Add or delete rules to your stream.
        rules should be in the form:
            [{'value': ''},{'tag':''}] if `update` is add
            {'ids':[""]} OR {'values':[""]} if `update` is delete

        """
        if len(rules) == 0:
            raise Exception('no rules to updates')

        body = {update: rules}
        return makePostApiCall(url, data=body, headers=self.headers, debug=self.debug)


    def retrieveRules(self, ids):
        """
        Return a list of rules currently active on the streaming endpoint, either as a list or individually.
        """
        url = self.base_url + '/tweets/search/stream/rules'
        params = {}
        if ids:
            params.update({'ids':ids})

        return makeGetApiCall(url, params=params, headers=self.headers, debug=self.debug)


    def connectStream(self, expansions=None, tweet_fields=None, media_fields=None, place_fields=None, poll_fields=None, user_fields=None):
        """Streams Tweets in real-time based on a specific set of filter rules. """

        url = self.base_url + '/tweets/search/stream'

        return makeGetApiCall(url, headers=self.headers, debug=self.debug)


