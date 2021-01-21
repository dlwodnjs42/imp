from server.social_api.instagram.core_api import InstagramCoreApi

from decouple import config
from social_api.util import makeGetApiCall, displayApiCallData, setRequestParams, makePostApiCall

import requests
import json

"""

Represents an Instagram Business Account or an Instagram Creator Account.

This node allows you to:

get an IG User's metadata
discover information about other Instagram Business IG Users
determine the IG Hashtags that an IG User has recently searched for
get insights on an IG User
get all IG Media objects on an IG User
get all story IG Media objects on an IG User
get data on IG Media objects on which an IG User has been tagged
get data on IG Comments on which an IG User has been @mentioned
get data about IG Media objects on which an IG User has been @mentioned in a caption
reply to IG Comments or captioned IG Media objects on which an IG User has been @mentioned

https://developers.facebook.com/docs/instagram-api/reference/user
"""

class UserApi(InstagramCoreApi):
    def getUserMedia(self, ref, data_fields=None, pagingUrl=''):
        """
        ref = (tags, stories, recently_searched_hashtags, media)
        API Endpoint:
            https://graph.facebook.com/{graph-api-version}/{ig-user-id}/{ref}?fields={fields}&access_token={access-token}

        Returns object: data from the endpoint
        """

        if not data_fields:
            # set default fields
            data_fields = '{id,caption,media_type,media_url,permalink,thumbnail_url,timestamp,username}'

        params = {
            'fields': data_fields,
            'access_token': self.user_access_token
        }

        url = self.url + self.instagram_account_id + '/media'
        return makeGetApiCall(url, params, debug=self.debug)

    def replyToMentionedInMediaObjectCaption(self, media_id, message)
        """ Creates an IG Comment on an IG Media object in which an IG User has been @mentioned in a caption.  """

        params = {
            'media_id': media_id,
            'message': message,
            'access_token': self.user_access_token
        }

        url = self.url + self.instagram_account_id + '/mentions'
        return makePostApiCall(url, params, debug=self.debug)

    def replyToMentionedInMediaObjectComment(self, media_id, comment_id, message)
        """ Creates an IG Comment on an IG Comment in which an IG User has been @mentioned.  """

        params = {
            'media_id': media_id,
            'message': message,
            'comment_id': comment_id,
            'access_token': self.user_access_token
        }

        url = self.url + self.instagram_account_id + '/mentions'
        return makePostApiCall(url, params, debug=self.debug)

    def readMentionedInComment(self, comment_id, data_fields=None):
        """
        Returns data on an IG Comment in which an IG User has been @mentioned by another Instagram user.

        Limitations
            This endpoint will return an error if comments have been disabled on the IG Media on which the IG User has been @mentioned.

        Field Expansion:
            - media

        TODO: Pagination
        """

        if not data_fields:
            data_fields = '{id,like_count,media{id,media_url},text,timestamp}'

        params = {
            'fields': 'mentioned_comment.comment_id(' + comment_id + ')' + data_fields
            'access_token': self.user_access_token
        }

        url = self.url + self.instagram_account_id
        return makeGetApiCall(url, params, debug=self.debug)

    def readMentionedInMedia(self, media_id, data_fields=None):
        if not data_fields:
            data_fields = '{caption,comments,comment_count,id,like_count,media_type,media_url,owner,timestamp,username}'

        params = {
            'fields': 'mentioned_media.media_id(' + media_id + ')' + data_fields
            'access_token': self.user_access_token
        }

        url = self.url + self.instagram_account_id
        return makeGetApiCall(url, params, debug=self.debug)


    def findRecentlySearchedHashtags(self):
        """
        Get the IG Hashtags that an IG User has searched for within the last 7 days. You can query a maximum of 30 unique hashtags on behalf of a user within a rolling, 7 day period. A queried hashtag will count against that user's limit as soon as it is queried. Subsequent queries on that hashtag within 7 days of the initial query will not count against the user's limit.

        Limitations
            Emojis in hashtag queries are not supported.
            The API returns 25 results per page by default, but you can use the limit parameter to get up to 30 per page (limit=30).
        """
        url = self.url + self.instagram_account_id + '/' + 'recently_searched_hashtags'
        return makeGetApiCall(url, params, debug=self.debug)


    def getIGUserMetadata(self, username):
        params = {
            'fields': 'business_discovery.username(' + username + ')'
            'access_token': self.user_access_token
        }

        url = self.url + self.instagram_account_id
        return makeGetApiCall(url, params, debug=self.debug)

    def getIGUserMedia(self, username, data_fields=None):
        if not data_fields:
            data_fields = "{biography,id,ig_id,followers_count,follows_count,media_count,name,profile_picture_url,username,website}"

        params = {
            'fields': 'business_discovery.username(' + username + ')' + data_fields
            'access_token': self.user_access_token
        }

        url = self.url + self.instagram_account_id
        return makeGetApiCall(url, params, debug=self.debug)

    # def getUserMetadata(self, data_fields=None):
    #     if not data_fields:
    #             # set default fields
    #             data_fields = '{id,biography,ig_id,followers_count,follows_count,media_count,name,profile_picture_url,username,website}'

    #     params = {
    #         'fields': data_fields,
    #         'access_token': self.user_access_token
    #     }

    #     url = self.url + self.instagram_account_id + '/'
    #     return makeGetApiCall(url, params, debug=self.debug)


    def getUserComments(self, media_id, data_fields=None):
        """
        Grab comments of a media object.
        Limitations:
            Fields that return aggregated values will not include ads-driven data. For example, comments_count will count comments on a photo, but not comments on ads that contain that photo.
            Captions will not include the (@) symbol unless the app user is also able to perform Admin-equivalent Tasks on the app.
            Some Fields cannot be used on Photos within Albums (children).
            The media_url field will be omitted from responses if the IG Media contains copyrighted material or has been flagged for a copyright violation.
            IGTV and Reels are not supported.
        """
        if not data_fields:
            data_fields = '{hidden,id,like_count,media,replies,text,timestamp,user,username}'

        params = {
            'fields': data_fields,
            'access_token': self.user_access_token
        }

        url = self.url + self.instagram_account_id + '/' + comment_id
        return makeGetApiCall(url, params, debug=self.debug)

    def getUserInsights(self, metric, period, since=None, until=None, data_fields=None, limit=10):
        """
        List of metrics and periods: https://developers.facebook.com/docs/instagram-api/reference/user/insights

        since/until are Unix timestamps.
        """
        if ref == 'media':
            if not data_fields:
                data_fields= '{description,id,name,period,title,values}'

        if ref == 'hashtag'

        metric

        params = {
            'fields': data_fields,
            'metric': metric,
            'period': period,
            'limit': limit,
            'access_token': self.user_access_token
        }

        if since and update:
            params.update({'since': since, 'update':update})

        url = self.url + self.instagram_account_id + '/insights'
        return makeGetApiCall(url, params, debug=self.debug)

    def getUserStories(self, data_fields=None):
        """ Returns a list of story IG Media objects on an IG User. """
        if not data_fields:
            data_fields = '{comments_count,caption,id,is_comment_enabled,ig_id,media_type,media_url,permalink,owner,like_count,thumbnail_url,shortcode,username}'

        params = {
            'fields': data_fields,
            'access_token': self.user_access_token
        }

        url = self.url + self.instagram_account_id + '/stories'
        return makeGetApiCall(url, params, debug=self.debug)

    def getUserTags(self, data_fields=None):
        """ Returns a list of IG Media objects in which an IG User has been tagged by another Instagram user. """
        if not data_fields:
            data_fields='{caption,comments,comments_count,id,like_count,media_type,media_url,owner,timestamp,username}'

        params = {
            'fields': data_fields,
            'access_token': self.user_access_token
        }

        url = self.url + self.instagram_account_id + '/tags'
        return makeGetApiCall(url, params, debug=self.debug)
