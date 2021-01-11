from social_api.util import makeGetApiCall, displayApiCallData, setRequestParams, makePostApiCall
from social_api.twitter.core_api import TwitterCoreApi

"""
The RESTful endpoint uses the GET method to return information about a user or group of users, specified by a user ID or a username. The response includes one or many user objects, which deliver fields such as the Follower count, location, pinned Tweet ID, and profile bio. Responses can also optionally include expansions to return the full Tweet object for a user’s pinned Tweet, including the Tweet text, author, and other Tweet fields.

This endpoint is commonly used to receive up-to-date details on a user, to verify that a user exists, or to update your stored details following a compliance event.

https://developer.twitter.com/en/docs/twitter-api/users/lookup/introduction
"""

class UserLookUpAPI(TwitterCoreApi):

    def getMultipleUserData(self, ids, expansions=None, tweet_fields=None, user_fields=None):
        """ Returns a variety of information about one or more users specified by the requested IDs. """

        url = self.base_url + '/users'
        params = {'ids': ids}

        if expansions:
            params.update({'expansions':expansions})
        if tweet_fields:
            params.update({'tweet_fields':tweet_fields})
        if user_fields:
            params.update({'user_fields': user_fields})

        return makeGetApiCall(url, params=params, header=self.header, debug=self.debug)

    def getSingleUserData(self, id, expansions=None, tweet_fields=None, user_fields=None):
        """ Returns a variety of information about one or more users specified by the ID. """
        url = self.base_url + f'/users/{id}'

        if expansions:
            params.update({'expansions':expansions})
        if tweet_fields:
            params.update({'tweet_fields':tweet_fields})
        if user_fields:
            params.update({'user_fields': user_fields})

        return makeGetApiCall(url, params=params, header=self.header, debug=self.debug)

    def getUsersByUserNames(self, usernames, expansions=None, tweet_fields=None, user_fields=None)
        """ Returns a variety of information about one or more users specified by their usernames. """
        url = self.base_url + '/users/by'
        params = {'usernames': usernames}

        if expansions:
            params.update({'expansions':expansions})
        if tweet_fields:
            params.update({'tweet_fields':tweet_fields})
        if user_fields:
            params.update({'user_fields': user_fields})

        return makeGetApiCall(url, params=params, header=self.header, debug=self.debug)

    def getUserByUserName(self, username, expansions=None, tweet_fields=None, user_fields=None)
        """ Returns a variety of information about one or more users specified by their usernames. """
        url = self.base_url + f'/users/by/username/{username}'

        if expansions:
            params.update({'expansions':expansions})
        if tweet_fields:
            params.update({'tweet_fields':tweet_fields})
        if user_fields:
            params.update({'user_fields': user_fields})

        return makeGetApiCall(url, params=params, header=self.header, debug=self.debug)
