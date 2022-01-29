from facebook_business.adobjects.adaccount import AdAccount

from facebook_business.adobjects.campaign import Campaign
from facebook_business.adobjects.adset import AdSet
from facebook_business.adobjects.ad import Ad
from facebook_business.adobjects.adcreative import AdCreative
from facebook_business.adobjects.page import Page
from facebook_business.adobjects.pagepost import PagePost

from facebook_business.api import FacebookAdsApi

access_token = '{ACCES-TOKEN}'
app_secret = '{APP-SECRET}'
app_id = '{APP_ID}'
id = '{AD_ACCPUNT_ID}'
FacebookAdsApi.init(access_token=access_token)


from facebook_business.adobjects.adaccount import AdAccount

from facebook_business.adobjects.campaign import Campaign
from facebook_business.adobjects.adset import AdSet
from facebook_business.adobjects.ad import Ad
from facebook_business.adobjects.adcreative import AdCreative
from facebook_business.adobjects.page import Page
from facebook_business.adobjects.pagepost import PagePost

from facebook_business.api import FacebookAdsApi

access_token = 'EAAQmOO1AkaoBAPbES3ZCGvwMk6dcnOCCetbAB9e3Fwxm9balFkXZAUKP8mKAMMx4qU3OR1zJvjuGX6iOb30Au778xNcOsZAqWIF1YByf44GoC7uIi1KOBUGLDUMXqKjoZAjyV41v41fHNlrLJ94nu5X8bcNx1W836XtZAFpvccyoZBaFN78jdlTa3X0XqbtY8vmQAllAk9AgZDZD'
app_secret = '3c074e1ee7a8239f64bf469eed224d05'
app_id = '1167925847298474'
id = 'act_68601302'
FacebookAdsApi.init(access_token=access_token)


def create_campaigns():
    name = str(input('Campaign Name: '))
    print('NONE, EMPLOYMENT, HOUSING, CREDIT, ISSUES_ELECTIONS_POLITICS, ONLINE_GAMBLING_AND_GAMING')
    special_ad_categories = str(input('Special Ad Categories: '))
    print(
        'Use one of: APP_INSTALLS, BRAND_AWARENESS, EVENT_RESPONSES, LEAD_GENERATION, LINK_CLICKS, LOCAL_AWARENESS, MESSAGES, OFFER_CLAIMS, PAGE_LIKES, POST_ENGAGEMENT, PRODUCT_CATALOG_SALES, REACH, STORE_VISITS, VIDEO_VIEWS, CONVERSIONS.')
    objective = str(input('Campaign objective: '))
    print('PAUSED')
    status = str(input('Status: '))

    fields = [
        'name',
    ]
    params = {
        'name': name,
        'objective': objective,
        'status': status,
        'special_ad_categories': special_ad_categories,
    }

    data = AdAccount(id).create_campaign(fields=fields, params=params)
    print(data)


# create_campaigns()


def create_ad_sets():
    campaign_id = str(input('Campaign ID: '))
    name = str(input('Ad set name: '))

    lifetime_budget = str(input('Lifetime Budget: '))
    start_time = str(input('Start Date: '))
    end_time = str(input('End Date: '))

    optimization_goal = str(input('Optimization for ad delivery: '))
    bid_amount = str(input('Bid control (optional): '))

    status = str(input('Status: '))

    fields = [
        'name',
    ]
    params = {
        'name': name,
        'lifetime_budget': lifetime_budget,
        'start_time': start_time,
        'end_time': end_time,
        'campaign_id': campaign_id,
        'bid_amount': bid_amount,
        'billing_event': 'IMPRESSIONS',
        'optimization_goal': optimization_goal,
        'targeting': {
            'age_min': 20,
            'age_max': 24,
            'behaviors': [{'id': 6002714895372, 'name': 'All travelers'}],
            'genders': [1],
            'geo_locations': {'countries': ['US'],
                              'regions': [{'key': '4081'}],
                              'cities': [{'key': '777934', 'radius': 10, 'distance_unit': 'mile'}]},
            'interests': [{'id': '6003139266461', 'name': 'Movies'}],
            'life_events': [{'id': 6002714398172, 'name': 'Newlywed (1 year)'}],
            'facebook_positions': ['feed'],
            'publisher_platforms': ['facebook', 'audience_network']},
        'status': status,
    }

    data = AdAccount(id).create_ad_set(fields=fields, params=params)
    print(data)


# create_ad_sets()


def ad_creative():
    name = str(input('Creative Name: '))
    page_id = str(input('Page ID: '))
    image_hash = str(input('Image Hash: '))
    website_url = str(input('Website URL: '))
    primary_text = str(input('Primary text: '))
    headline = str(input('Headline: '))
    description = str(input('Description: '))

    fields = [
        'name',
    ]

    params = {
        'name': name,
        'object_story_spec': {'page_id': page_id,
                              'link_data': {
                                  'image_hash': image_hash,
                                  'link': website_url,
                                  'message': primary_text,
                                  'name': headline,
                                  "description": description,
                              }},
    }
    data = AdAccount(id).create_ad_creative(fields=fields, params=params)
    print(data)


# ad_creative()


def create_ads():
    ad_set_id = str(input('Adset ID: '))
    name = str(input('Ad Name: '))
    creative_id = str(input('Creative ID: '))
    status = str(input('Status: '))

    fields = [
        'name',
        'preview_shareable_link',

    ]
    params = {
        'name': name,
        'ad_set_id': ad_set_id,
        'creative': {'creative_id': creative_id},
        'status': status,
    }

    data = AdAccount(id).create_ad(fields=fields, params=params)
    print(data)


# create_ads()


def call_campaigns():
    fields = [
      'name',
      'objective',
    ]
    params = {
      'effective_status': ['PAUSED'],
    }
    data = AdAccount(id).get_campaigns(fields=fields, params=params)
    print(data)


# call_campaigns()


def call_ad_sets():
    fields = [
        'name',
        'start_time',
        'end_time',
        'daily_budget',
        'lifetime_budget',
        'delivery_estimate'
    ]

    params = {}

    return Campaign(id).get_ad_sets(fields=fields, params=params)


response = call_ad_sets()
print(response)


# call_ad_sets()


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


def create_carousel():
  fields = [
  ]
  params = {
    'message': 'Browse our latest products',
    'published': '0',
    'child_attachments': [{
      'link': '<link>',
      'name': 'Product 1',
      'description': '$4.99',
      'image_hash': '<imageHash>'
    },
      {
        'link': '<link>',
        'name': 'Product 2',
        'description': '$4.99',
        'image_hash': '<imageHash>'
      },
      {
        'link': '<link>',
        'name': 'Product 3',
        'description': '$4.99',
        'image_hash': '<imageHash>'
      },
      {
        'link': '<link>',
        'name': 'Product 4',
        'description': '$4.99',
        'image_hash': '<imageHash>'
      },
    ],
    'caption': 'WWW.EXAMPLE.COM',
    'link': 'http://www.example.com/products',
  }

  data = Page(id).get_posts(fields=fields, params=params)
  print(data)


create_carousel()
