"""
RATELIMIT:
300 requests per 15-minute window (app auth)
900 requests per 15-minute window (user auth)

AUTH SUPPORTED:
OAuth 1.0a User context
OAuth 2.0 Bearer token

URL:
https://developer.twitter.com/en/docs/twitter-api/tweets/lookup/api-reference/get-tweets

"""

from social_api.util import makeGetApiCall, displayApiCallData, setRequestParams, makePostApiCall
from social_api.twitter.core_api import TwitterCoreApi
from social_api.twitter.tweets.util import get_all_params

class TweetApi(TwitterCoreApi):
    def getTweets(self, ids, expansions=None, tweet_fields=None, media_fields=None, place_fields=None, poll_fields=None, user_fields=None):
        """
        Returns a variety of information about the Tweet specified by the list of IDs.
        """

        url = self.base_url + '/tweets'
        params = {'ids': ids}
        params = get_all_params(
            params, expansions,tweet_fields,media_fields,place_fields,poll_fields,user_fields)

        return makeGetApiCall(url, params=params, headers=self.headers, debug=self.debug)

    def getTweet(self, id, expansions=None, tweet_fields=None, media_fields=None, place_fields=None, poll_fields=None, user_fields=None):
        """
        Returns a variety of information about the Tweet specified by the requested ID
        """
        url = self.base_url + '/tweets' + '/' + id
        params = {'id': id} if id else {}
        params = get_all_params(
            params, expansions,tweet_fields,media_fields,place_fields,poll_fields,user_fields)

        return makeGetApiCall(url, params=params, headers=self.headers, debug=self.debug)


