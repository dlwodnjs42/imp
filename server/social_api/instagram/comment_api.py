from server.social_api.instagram.core_api import InstagramCoreApi

from decouple import config
from social_api.util import makeGetApiCall, displayApiCallData, setRequestParams, makePostApiCall

import requests
import json

"""
Represents a comment on an IG Media object.

This node allows you to:

read a comment's metadata
hide or delete individual comments.
reply to a comment
get all replies to a comment

"""

class CommentApi(InstagramCoreApi):

    def enableDisableComments(media_id, comment_enabled):
        """ Enables and Disables comments on a media object """
        params = {
            'comment_enabled': comment_enabled,
            'access_token': self.user_access_token
        }

        url = self.url + media_id
        return makePostApiCall(url, params, debug=self.debug)

    def getAllCommentReplies(self, comment_id, data_fields):
        params = {
            'access_token': self.user_access_token
        }
        url = self.url + comment_id + '/replies'
        return makeGetApiCall(url, params, debug=self.debug)

    def replyToComment(self, comment_id, message):
        params = {
            'message': message
            'access_token': self.user_access_token
        }
        url = self.url + comment_id + '/replies'
        return makePostApiCall(url, params, debug=self.debug)

    def hideComments(self, comment_id, hide)
        params = {
            'hide': hide,
            'access_token': self.user_access_token
        }

        url = self.url + comment_id
        return makePostApiCall(url, params, debug=self.debug)

    def deleteComments(self, comment_id):
        return makeDeleteApiCall(url, debug=self.debug)
