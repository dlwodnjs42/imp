from social_api.util import makeGetApiCall, displayApiCallData, setRequestParams, makePostApiCall
from social_api.twitter.core_api import TwitterCoreApi
"""
Following users is one of the most foundational actions on Twitter; users can keep up to date with their relevant connections by following other users on Twitter. At a larger scale, this creates a network of connections between users.

The follows lookup endpoints enable you to explore and analyze the relationships between users, which is sometimes called network analysis. Specifically, there are two RESTful endpoints that return user objects representing who a specified user is following, or who is following a specified user.

You can authenticate these endpoints with either OAuth 1.0a User Context or OAuth 2.0 Bearer Token. Also, you can request up to 1000 users per request, and pagination tokens will be provided for paging through large sets of matching Tweets.

15 requests per 15-minute window (app auth)
15 requests per 15-minute window (user auth)

https://developer.twitter.com/en/docs/twitter-api/users/follows/introduction
"""
class FollowsAPI(TwitterCoreApi):

    def findUserFollowing(self, id, max_results=None, pagination_token=None, expansions=None, tweet_fields=None, user_fields=None):
        """ Returns a list of users the specified user ID is following."""
        if max_results:
            params.update({'max_results': max_results})
        if pagination_token:
            params.update({'pagination_token': pagination_token})
        if expansions:
            params.update({'expansions':expansions})
        if tweet_fields:
            params.update({'tweet_fields':tweet_fields})
        if user_fields:
            params.update({'user_fields': user_fields})

        url = self.base_url + f'/users/{id}/following'

        return makeGetApiCall(url, params=params, header=self.header, debug=self.debug)

    def findUserFollowers(self, id):
        if max_results:
            params.update({'max_results': max_results})
        if pagination_token:
            params.update({'pagination_token': pagination_token})
        if expansions:
            params.update({'expansions':expansions})
        if tweet_fields:
            params.update({'tweet_fields':tweet_fields})
        if user_fields:
            params.update({'user_fields': user_fields})

        url = self.base_url + f'/users/{id}/following'

        return makeGetApiCall(url, params=params, header=self.header, debug=self.debug)
