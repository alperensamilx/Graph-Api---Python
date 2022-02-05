from facebook_business.adobjects.adaccount import AdAccount
from facebook_business.adobjects.adcreative import AdCreative
from facebook_business.api import FacebookAdsApi

access_token = ''
app_secret = ''
app_id = ''
id = ''
FacebookAdsApi.init(access_token=access_token)

def create_video():
    fields = [
    ]
    params = {
        'name': 'Video Creative',

        'object_story_spec': {'page_id': '103122378948499',
                              'video_data': {
                                  'image_url': 'https://scontent.fist4-1.fna.fbcdn.net/v/t1.18169-9/11701119_1096804877014160_4246085576298344409_n.jpg?_nc_cat=111&ccb=1-5&_nc_sid=09cbfe&_nc_ohc=RU_deGQrNEkAX9KwO2B&_nc_ht=scontent.fist4-1.fna&oh=00_AT-NqO6aiivQOOQ6eyzi9ShJmQqLh51BAUc-ABfyYPo5yQ&oe=62150B12',
                                  'video_id': '352843156367900',
                                  'call_to_action': {'type': 'LIKE_PAGE', 'value': {'page': '103122378948499'}}
                              },

                              },
    }
    data = AdAccount(id).create_ad_creative(fields=fields, params=params)
    print(data)

# create_video()
