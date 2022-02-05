from facebook_business.adobjects.adaccount import AdAccount
from facebook_business.adobjects.adcreative import AdCreative
from facebook_business.api import FacebookAdsApi

access_token = '{ACCES-TOKEN}'
app_secret = '{APP-SECRET}'
app_id = '{APP_ID}'
id = '{AD_ACCPUNT_ID}'
FacebookAdsApi.init(access_token=access_token)

def create_video():
    print('103122378948499')
    page_id = str(input("Page ID: "))
    print('https://scontent.fist4-1.fna.fbcdn.net/v/t1.18169-9/11701119_1096804877014160_4246085576298344409_n.jpg?_nc_cat=111&ccb=1-5&_nc_sid=09cbfe&_nc_ohc=RU_deGQrNEkAX9KwO2B&_nc_ht=scontent.fist4-1.fna&oh=00_AT-NqO6aiivQOOQ6eyzi9ShJmQqLh51BAUc-ABfyYPo5yQ&oe=62150B12')
    image_url = str(input("Image URL: "))
    print('5167895076567743')
    video_id = str(input('Video ID: '))
    print('LIKE_PAGE')
    call_to_action = str(input("Call to Action: "))

    fields = [
    ]
    params = {
        'name': 'Video Creative',

        'object_story_spec': {'page_id': page_id,
                              'video_data': {
                                          'image_url': image_url,
                                          'video_id': video_id,
                                          'call_to_action': {'type': call_to_action, 'value': {'page': page_id}}
                                            },


                              },
    }
    data = AdAccount(id).create_ad_creative(fields=fields, params=params)
    print(data)


# create_video()
