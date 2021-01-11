from social_api.util import makeGetApiCall, displayApiCallData, setRequestParams, makePostApiCall
from social_api.twitter.core_api import TwitterCoreApi

"""
The sampled stream endpoint delivers a roughly 1% random sample of publicly available Tweets in real-time. With it, you can identify and track trends, monitor general sentiment, monitor global events, and much more.

This streaming endpoint delivers Tweet objects through a persistent HTTP GET connection, and uses OAuth 2.0 Bearer Token authentication. You can connect one client per session, and can disconnect and reconnect no more than 50 times per 15 minute window.


https://developer.twitter.com/en/docs/twitter-api/tweets/sampled-stream/api-reference/get-tweets-sample-stream
"""

class SampledStreamApi(TwitterCoreApi):
    def connectStream(self, expansions=None, tweet_fields=None, media_fields=None, place_fields=None, poll_fields=None, user_fields=None):
        """Streams Tweets in real-time based on a specific set of filter rules. """

        url = self.base_url + '/tweets/search/stream'

        return makeGetApiCall(url, header=self.headers, debug=self.debug)
