import requests
import json
from instagram.instagram_api import InstagramCoreApi

from decouple import config







if __name__ == "__main__":
    instagram = InstagramCoreApi(
        token=config('ACCESS_TOKEN'),
        user_id=config('USER_ID'),
        page_id=config('PAGE_ID'),
        ig_username='impte.mp',
        debug=True
        )
    response = instagram.getAccountInfo()
