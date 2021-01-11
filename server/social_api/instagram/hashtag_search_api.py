from server.social_api.instagram.core_api import InstagramCoreApi

from decouple import config
from social_api.util import makeGetApiCall, displayApiCallData, setRequestParams, makePostApiCall

import requests
import json

"""
This root edge allows you to get IG Hashtag IDs.

https://developers.facebook.com/docs/instagram-api/reference/ig-hashtag-search
"""
class HashtagSearchApi(InstagramCoreApi):

    def getHashTagSearch(self, user_id, q):
        """
        {user_id} (required) — The ID of the IG User performing the request.
        {q} (required) — The hashtag name to query.
        Returns the ID of an IG Hashtag. IDs are both static and global (i.e, the ID for #bluebottle will always be 17843857450040591 for all apps and all app users).
        NOTE:You can query a maximum of 30 unique hashtags within a 7 day period.
        The API will return a generic error for any queries that include hashtags that we have deemed sensitive or offensive.

        """
        params = {
            'user_id': user_id,
            'q': q,
            'access_token': self.user_access_token
        }

        url = self.url + 'ig_hashtag_search'
        return makePostApiCall(url, params, debug=self.debug)

