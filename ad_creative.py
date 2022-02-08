from facebook_business.adobjects.adaccount import AdAccount
from facebook_business.adobjects.adcreative import AdCreative
from facebook_business.api import FacebookAdsApi



access_token = 'EAAQmOO1AkaoBAFUNjoZCErBfAn3VOyqdNSDwh0DXwEruXy2TOUgNDYyrqIsfCXAb6k1Ndd6PZATIeZBJZAQImXTEOZBkZAhhDVDg2QdxLyfmHwj2cn0M6K5RQDYRvLwXZCJcIJ0urmPABCFhf3lOU8J7k0YvbwEkUjgFuNy5OI9UvhpU9CPHTGcqhWCTZBs8nNVjyNmBXVXZA2t6TXDCLZCvY6'
app_secret = '3c074e1ee7a8239f64bf469eed224d05'
app_id = '1167925847298474'
id = 'act_68601302'
FacebookAdsApi.init(access_token=access_token)


# Ad Creative
def ad_creative():
    name = str(input('Creative Name: '))
    print('103122378948499')
    page_id = str(input('Page ID: '))
    print('https://www.facebook.com/photo/?fbid=1096804877014160&set=a.151184061576251')
    image_hash = str(input('Image Hash: '))
    website_url = str(input('Website URL: '))
    primary_text = str(input('Primary text: '))
    headline = str(input('Headline: '))
    description = str(input('Description: '))
    print('LEARN_MORE')
    call_to_action = str(input("Call to Action: "))

    fields = [
        'name',
    ]

    params = {
        'name': name,
        'object_story_spec': {'page_id': page_id,
                              'link_data': {
                                  'image_file': image_hash,
                                  'link': website_url,
                                  'message': primary_text,
                                  'name': headline,
                                  "description": description,
                                  "call_to_action": {
                                      "type": call_to_action
                                  }

                              }},
    }
    data = AdAccount(id).create_ad_creative(fields=fields, params=params)
    print(data)


ad_creative()

