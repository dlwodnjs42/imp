from server.social_api.instagram.core_api import InstagramCoreApi

from decouple import config
from social_api.util import makeGetApiCall, displayApiCallData, setRequestParams, makePostApiCall

import requests
import json

"""
Represents an Instagram Photo, Video, Story, or Album. IGTV and Reels are not supported.

This Node allows you to:

get metadata for individual media objects
toggle comments on or off for individual media objects
create comments on individual media objects
get all child media objects in an album carousel
get all comments for individual media objects
get all insights for individual media objects

https://developers.facebook.com/docs/instagram-api/reference/media

"""

class MediaApi(InstagramCoreApi):

    def createComments(self, media_id, message):
        """ Creates an IG Comment on an IG Media object."""
        params = {
            'message': message,
            'access_token': self.user_access_token
        }

        url = self.url + media_id + '/comments'
        return makePostApiCall(url, params, debug=self.debug)

    def getMediaObjectComments(self, media_id):
        """ Returns a list of IG Comments on an IG Media object. """
        params = {
            'access_token': self.user_access_token
        }

        url = self.url + media_id + '/comments'
        return makeGetApiCall(url, params, debug=self.debug)


    def getChildrenMediaObjects(self, media_id):
        """ Returns a list of IG Media objects on an album IG Media object. """
        params = {
            'access_token': self.user_access_token
        }

        url = self.url + media_id + '/children'
        return makeGetApiCall(url, params, debug=self.debug)

    def getMediaObjectInsights(self, media_id, metric):
        """ Get insights data on an IG Media object. Values for each metric are calculated at the time of the request.

        Limitations
            - Insights data is not available for IG Media objects within album IG Media objects.
            Story IG Media object insights are only available for 24 hours, even if the stories are archived or highlighted. If you want to get the latest insights for a story before it expires, set up a Webhook for the Instagram topic and subscribe to the story_insights field.
            - Story IG Media object metrics with values less than 5 will return an error code 10 with the message (#10) Not enough viewers for the media to show insights.

        See for metric choices:
        https://developers.facebook.com/docs/instagram-api/reference/media/insights

        """
        params = {
            'access_token': self.user_access_token
        }

        url = self.url + media_id + '/insights'
        return makeGetApiCall(url, params, debug=self.debug)




