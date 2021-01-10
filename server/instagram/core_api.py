from decouple import config
from instagram.util import makeGetApiCall, displayApiCallData, setRequestParams

import requests
import json

class InstagramCoreAPI:
    def __init__(self, token, ig_username, user_id, page_id, ig_acc_id=None, debug=False):
        self.url = self.createBaseUrl()

        self.user_access_token = token
        self.instagram_username = ig_username

        # ids
        self.page_id = page_id
        self.user_id = user_id

        self.instagram_account_id = self.getInstagramAccountId(ig_acc_id)
        self.debug = debug

    def createBaseUrl(self):
        base_url = "https://graph.facebook.com/"
        version = "v9.0"
        return base_url + version + '/'

    def getInstagramAccountId(self, instagram_account_id, debug=True):
        """
        Grab instagram account id from page_id and access token.
        GET "https://graph.facebook.com/v9.0/{page_id}?fields=connected_instagram_account&access_token={user_token}
        """
        if instagram_account_id:
            return instagram_account_id

        params = setRequestParams(fields='connected_instagram_account')

        response = makeGetApiCall(self.url + self.page_id, params, debug)

        account = response['json_data'].get('connected_instagram_account','')
        if "id" not in account:
            return account

        instagram_account_id = account['id']
        return instagram_account_id

    def getPageId(self, page_name, user_id, access_token, debug=True):
        """
        Grab Page Id from page_name, user_id and access token.
        GET https://graph.facebook.com/v9.0/10223398117842352/accounts?access_token=EAAC8CYgeaz8BAL5RWRQxNuhaIuaYp0PXMxq1G0e4Hm7sgA7ugw5c2L6zxTkMX5AFrdRuHVKFMcmAC17TqJ5JzSs81NJ5oDwaPGsh4oQ2YmVxWbjt7AJIjT4AVF4tnGyf5UxJGJnIy4k9aVmu5utuoQXxg2biwkViXjT8aAZDZD
        """

        params = setRequestParams()
        url = self.url + user_id + "/accounts?"
        response = makeGetApiCall(url, params, debug)

        for data in response['data']:
            if data.get('name') == page_name:
                return data.get('id')
        return ''

    def getAccountInfo(self, data_fields=None):
        """
        Get Account info:
            - username, website, name, ig_id, id, profile_picture_url, biography, follows_count, followers_count, media_count

        API Endpoint:
        https://graph.facebook.com/v9.0{user-id}?fields=business_discovery.username({username}){username,website,name,ig_id,id,profile_picture_url,biography,follows_count,followers_count,media_count}&&access_token={access_token}
        """
        if not fields:
            data_fields = '{username,website,name,ig_id,id,profile_picture_url,biography,follows_count,followers_count,media_count}'

        params = {
            'fields': 'business_discovery.username(' + self.instagram_username + ')' + data_fields,
            'access_token': self.user_access_token
        }
        url = self.url + self.instagram_account_id
        return makeGetApiCall(url, params, self.debug)

