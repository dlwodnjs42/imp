from social_api.util import makeGetApiCall, displayApiCallData, setRequestParams, makePostApiCall
from social_api.twitter.core_api import TwitterCoreApi
"""
The recent search endpoint returns Tweets from the last 7 days that match a search query.

https://developer.twitter.com/en/docs/twitter-api/tweets/search/api-reference/get-tweets-search-recent

450 requests per 15-minute window (app auth)
180 requests per 15-minute window (user auth)
"""
class RecentSearchAPI(TwitterCoreApi):
    def recentPublicSearch(self, query, since_id=None, start_time=None, max_results=None, end_time=None, next_token=None, until_id=None, expansions=None, tweet_fields=None, media_fields=None, place_fields=None, poll_fields=None, user_fields=None):
        """
        The recent search endpoint returns Tweets from the last 7 days that match a search query.

        At our Basic access level, you will be limited to receive 500,000 Tweets per month per project from either the filtered stream or search Tweets endpoints. For example, if you consumed 200,000 Tweets with filtered stream, you will be able to receive an additional 300,000 Tweets from either filtered stream or search Tweets. Once you have used up this allotment, you will need to wait until the next monthly period begins, which is set to the day that your developer account was approved.

        """
        params = {'query':query}
        if since_id:
            params.update({'since_id':since_id})
        if start_time:
            params.update({'start_time':start_time})
        if max_results:
            params.update({'max_results': max_results})
        if end_time:
            params.update({'end_time': end_time})
        if until_id:
            params.update({'until_id': until_id})
        if next_token:
            params.update({'next_token': next_token})

        params = get_all_params(
            params, expansions,tweet_fields,media_fields,place_fields,poll_fields,user_fields)
        url = self.base_url + '/tweets/search/recent'

        return makeGetApiCall(url, params=params, headers=self.headers, debug=self.debug)

