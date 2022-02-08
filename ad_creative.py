from facebook_business.adobjects.adaccount import AdAccount
from facebook_business.adobjects.adcreative import AdCreative
from facebook_business.api import FacebookAdsApi





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

