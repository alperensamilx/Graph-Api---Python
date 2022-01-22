from facebook_business.adobjects.adaccount import AdAccount
from facebook_business.adobjects.campaign import Campaign
from facebook_business.api import FacebookAdsApi

from facebookads.adobjects.adset import AdSet
from facebookads.adobjects.ad import Ad


access_token = '{access_token}'
app_secret = '{app_secret}'
app_id = '{app_id}'
id = '{id}'
FacebookAdsApi.init(access_token=access_token)


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


# call_ad_sets()


def call_ads():
    fields = [
        Ad.Field.name,
        Ad.Field.configured_status,
        Ad.Field.effective_status,
        Ad.Field.creative,
    ]

    params = {
        Ad.Field.effective_status: [
            'PAUSED'
        ],
    }

    ad_set = AdSet('6290943651216')
    ads = ad_set.get_ads(fields=fields)


# call_ads()


def create_campaigns():
    name = str(input('Campaign Name: '))
    objective = str(input('Objective: '))
    status = str(input('Status: '))
    special_ad_categoreies = list(input('Special Ad Categories: '))

    fields = [
        'name',
    ]
    params = {
        'name': 'My Python Campaign3',
        'objective': 'PAGE_LIKES',
        'status': 'PAUSED',
        'special_ad_categories': [],
    }

    data = (AdAccount(id).create_campaign(fields=fields, params=params))
    print(data)


# create_campaigns()


def create_ad_sets():
    fields = [
        'name',
    ]
    params = {
      'name': 'My Python AdSet',
      'lifetime_budget': '52500',
      'start_time': '2022-1-17T11:46:57-0800',
      'end_time': '2022-2-24T11:46:57-0800',
      'campaign_id': '6290943650816',
      'bid_amount': '1370',
      'billing_event': 'IMPRESSIONS',
      'optimization_goal': 'POST_ENGAGEMENT',
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
        'status': 'PAUSED',
    }

    data = (AdAccount(id).create_ad_set(fields=fields, params=params,))
    print(data)


# create_ad_sets()


def create_ad():
    fields = [
        'preview_shareable_link'
    ]
    params = {
        'name': 'My Python Ad',
        'adset_id': '6290943651216',
        'creative': {'creative_id': '6290953251416'},
        'status': 'PAUSED',
    }

    data = (AdAccount(id).create_ad(fields=fields, params=params,))
    print(data)


