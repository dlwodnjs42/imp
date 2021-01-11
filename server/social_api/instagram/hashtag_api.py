from server.social_api.instagram.core_api import InstagramCoreApi
from decouple import config
from social_api.util import makeGetApiCall, displayApiCallData, setRequestParams, makePostApiCall

import requests
import json

"""
Represents an Instagram hashtag.

https://developers.facebook.com/docs/instagram-api/reference/hashtag


You can query a maximum of 30 unique hashtags within a 7 day period.

"""


class HashtagApi(InstagramCoreApi):

    def getHashtag(self, hashtag_id, data_fields=None):
        """ Returns Fields and Edges on an IG Hashtag."""
        if not data_fields:
            data_fields = "{id,name}"

        params = {
            'fields': data_fields,
            'access_token': self.user_access_token
        }

        url = self.url + hashtag_id

        return makeGetApiCall(url, params, debug=self.debug)

    def getRecentMediaWithHashtag(self, hashtag_id, user_id, data_fields=None):
        """
        Represents a collection of the most recently published photo and video IG Media objects that have been tagged with a hashtag.

        Query String Parameters:
            {user_id} (required) — The ID of the IG User performing the query.
            {fields} — A comma-separated list of fields you want returned. See Returnable Fields.
        Limitations
            Only returns public photos and videos.
            Only returns media objects published within 24 hours of query execution.
            Will not return promoted/boosted/ads media.
            Responses are paginated with a maximum limit of 50 results per page.
            Responses will not always be in chronological order.
            You can query a maximum of 30 unique hashtags within a 7 day period.
            You cannot request the username field on returned media objects.
            Responses will not include any personally identifiable information.
            This endpoint only returns an after cursor for paginated results; a before cursor will not be included. In addition, the after cursor value will always be the same for each page, but it can still be used to get the next page of results in the result set.
        """
        if not data_fields:
            data_fields = "{caption,children,comments_count,id,like_count,media_type,media_url, permalink,timestamp,}"

        params = {
            'fields': data_fields,
            'user_id': user_id,
            'access_token': self.user_access_token
        }

        url = self.url + hashtag_id + '/recent_media'

        return makeGetApiCall(url, params, debug=self.debug)

    def getTopMediaWithHashtag(self, hashtag_id, user_id, data_fields=None):
        """
        Represents a collection of the most recently published photo and video IG Media objects that have been tagged with a hashtag.

        Query String Parameters:
            {user_id} (required) — The ID of the IG User performing the query.
            {fields} — A comma-separated list of fields you want returned. See Returnable Fields.
        Limitations
            Only returns public photos and videos.
            Only returns media objects published within 24 hours of query execution.
            Will not return promoted/boosted/ads media.
            Responses are paginated with a maximum limit of 50 results per page.
            Responses will not always be in chronological order.
            You can query a maximum of 30 unique hashtags within a 7 day period.
            You cannot request the username field on returned media objects.
            Responses will not include any personally identifiable information.
            This endpoint only returns an after cursor for paginated results; a before cursor will not be included. In addition, the after cursor value will always be the same for each page, but it can still be used to get the next page of results in the result set.
        """
        if not data_fields:
            data_fields = "{caption,children,comments_count,id,like_count,media_type,media_url, permalink,timestamp,}"

        params = {
            'fields': data_fields,
            'user_id': user_id,
            'access_token': self.user_access_token
        }

        url = self.url + hashtag_id + '/top_media'

        return makeGetApiCall(url, params, debug=self.debug)
