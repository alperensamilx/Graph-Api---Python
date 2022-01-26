from facebook_business.adobjects.adaccount import AdAccount

from facebook_business.adobjects.campaign import Campaign
from facebook_business.adobjects.adset import AdSet
from facebook_business.adobjects.ad import Ad
from facebook_business.adobjects.adcreative import AdCreative

from facebook_business.api import FacebookAdsApi

access_token = '{ACCES-TOKEN}'
app_secret = '{APP-SECRET}'
app_id = '{APP_ID}'
id = '{AD_ACCPUNT_ID}'
FacebookAdsApi.init(access_token=access_token)


def create_campaigns():
    name = str(input('Campaign Name: '))
    special_ad_categories = list(input('Special Ad Categories: '))
    objective = str(input('Campaign objective: '))
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

    data = (AdAccount(id).create_campaign(fields=fields, params=params))
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

    data = (AdAccount(id).create_ad_set(fields=fields, params=params, ))
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
    data = (AdAccount(id).create_ad_creative(fields=fields, params=params, ))
    print(data)


# ad_creative()


def create_ads():
    ad_set_id = str(input('Adset ID: '))
    name = str(input('Ad Name: '))
    creative_id = str(input('Creative ID: '))
    status = str(input('Status: '))

    fields = [
        'preview_shareable_link'
    ]
    params = {
        'name': name,
        'ad_set_id': ad_set_id,
        'creative': {'creative_id': creative_id},
        'status': status,
    }

    data = (AdAccount(id).create_ad(fields=fields, params=params,))
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
    data = AdAccount(id).get_campaigns(fields=fields, params=params,)
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

    data = Campaign(id).get_ad_sets(fields=fields, params=params)
    print(data)







# def create_campaigns():
#     fields = [
#         'name',
#     ]
#     params = {
#         'name': 'My Python Campaign4',
#         'objective': 'PAGE_LIKES',
#         'status': 'PAUSED',
#         'special_ad_categories': [],
#     }
#
#     data = (AdAccount(id).create_campaign(fields=fields, params=params))
#     print(data)
#
#
# create_campaigns()




# def create_ad_sets():
#     fields = [
#             'name',
#         ]
#     params = {
#             'name': 'My Python AdSet',
#             'lifetime_budget': '52500',
#             'start_time': '2022-1-17T11:46:57-0800',
#             'end_time': '2022-2-24T11:46:57-0800',
#             'campaign_id': '6290943650816',
#             'bid_amount': '1370',
#             'billing_event': 'IMPRESSIONS',
#             'optimization_goal': 'POST_ENGAGEMENT',
#             'targeting': {
#                 'age_min': 20,
#                 'age_max': 24,
#                 'behaviors': [{'id': 6002714895372, 'name': 'All travelers'}],
#                 'genders': [1],
#                 'geo_locations': {'countries': ['US'],
#                                   'regions': [{'key': '4081'}],
#                                   'cities': [{'key': '777934', 'radius': 10, 'distance_unit': 'mile'}]},
#                 'interests': [{'id': '6003139266461', 'name': 'Movies'}],
#                 'life_events': [{'id': 6002714398172, 'name': 'Newlywed (1 year)'}],
#                 'facebook_positions': ['feed'],
#                 'publisher_platforms': ['facebook', 'audience_network']},
#             'status': 'PAUSED',
#         }
#
#     data = (AdAccount(id).create_ad_set(fields=fields, params=params, ))
#     print(data)


# create_ad_sets()



# def create_ads():
#     fields = [
#         'preview_shareable_link'
#     ]
#     params = {
#         'name': 'My Python Ad5',
#         'adset_id': '6290943651216',
#         'creative': {'creative_id': '6291098407816'},
#         'status': 'PAUSED',
#     }
#
#     data = (AdAccount(id).create_ad(fields=fields, params=params,))
#     print(data)
#
#6291340340816
# create_ads()



# def ad_creative():
#     fields = [
#         'name',
#     ]

#     params = {
#         'name': 'Python Creative',
#         'object_story_spec': {'page_id': '103122378948499',
#                               'link_data': {
#                                   'image_hash': '',
#                                   'link': 'www.alperensamil.com',
#                                   'message': 'python message',
#                                   "description": 'Python description',
#                               }},
#     }
#     data = (AdAccount(id).create_ad_creative(fields=fields, params=params, ))
#     print(data)


# ad_creative()
