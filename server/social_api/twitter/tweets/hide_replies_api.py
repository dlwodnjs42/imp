from social_api.util import makeGetApiCall, displayApiCallData, setRequestParams, makePostApiCall, makePutApiCall
from social_api.twitter.core_api import TwitterCoreApi

"""

50 requests per 15-minute window (user auth)
"""

class HideRepliesApi(TwitterCoreApi):
    def hideReplies(self, id, hidden=False):
        """ Hides or unhides a reply to a Tweet. """

        url = self.base_url + f'/tweets/{id}/hidden'
        body = {'hidden': hidden}
        return makePutApiCall(url, data=body, header=self.header, debug=self.debug)
