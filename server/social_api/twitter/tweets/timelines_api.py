from social_api.util import makeGetApiCall, displayApiCallData, setRequestParams, makePostApiCall
from social_api.twitter.core_api import TwitterCoreApi
from social_api.twitter.tweets.util import get_all_params


class TimelineAPI(TwitterCoreApi):
    def getTweetTimelineByID(self, id, expansions=None, tweet_fields=None, media_fields=None, place_fields=None, poll_fields=None, user_fields=None):
        """
        Returns Tweets composed by a single user, specified by the requested user ID. By default, the most recent 10 Tweets are returned per request with the default Tweet id and text. Using pagination, the most recent 3,200 Tweets can be retrieved.
        """
        url = self.base_url + f'/users/{id}/tweets'
        params = get_all_params(
            {}, expansions, tweet_fields, media_fields, place_fields, poll_fields, user_fields)
        return makeGetApiCall(url, params=params, headers=self.headers, debug=self.debug)

    def getMentionTimelineByID(self, id, expansions=None, tweet_fields=None, media_fields=None, place_fields=None, poll_fields=None, user_fields=None):
        url = self.base_url + f'/users/{id}/mentions'
        params = get_all_params(
            {}, expansions, tweet_fields, media_fields, place_fields, poll_fields, user_fields)

        return makeGetApiCall(url, params=params, headers=self.headers, debug=self.debug)
