from facebook_business.adobjects.adaccount import AdAccount
from facebook_business.adobjects.adset import AdSet
from facebook_business.api import FacebookAdsApi

access_token = 'acces-token'
app_secret = 'app-secret'
app_id = 'app-id'
id = 'ad-account-id'
FacebookAdsApi.init(access_token=access_token)

def create_ad_sets():
    campaign_id = str(input('Campaign ID: '))
    name = str(input('Ad set name: '))
    print('Budget & schedule')
    lifetime_budget = str(input('Lifetime Budget: '))
    start_time = str(input('Start Date: '))
    end_time = str(input('End Date: '))
    print('Audience')
    age_min = str(input('Age Min: '))
    age_max = str(input('Age Max: '))

    print('IMPRESSIONS')
    billing_event = str(input('Billing Event: '))

    print('Optimization & delivery')
    print('{NONE, APP_INSTALLS, AD_RECALL_LIFT, ENGAGED_USERS, EVENT_RESPONSES, IMPRESSIONS, LEAD_GENERATION, QUALITY_LEAD, LINK_CLICKS, OFFSITE_CONVERSIONS, PAGE_LIKES, POST_ENGAGEMENT, QUALITY_CALL, REACH, LANDING_PAGE_VIEWS, VISIT_INSTAGRAM_PROFILE, VALUE, THRUPLAY, DERIVED_EVENTS, APP_INSTALLS_AND_OFFSITE_CONVERSIONS, CONVERSATIONS, IN_APP_VALUE}')
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
        'billing_event': billing_event,
        'optimization_goal': optimization_goal,
        'targeting': {
            'age_min': age_min,
            'age_max': age_max,
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


create_ad_sets()

