from facebook_business.adobjects.adaccount import AdAccount
from facebook_business.adobjects.adset import AdSet
from facebook_business.api import FacebookAdsApi

access_token = 'acces-token'
app_secret = 'app-secret'
app_id = 'app-id'
id = 'ad-account-id'
FacebookAdsApi.init(access_token=access_token)

fields = [
]
params = {
  'name': 'My Python AdSet',
  'lifetime_budget': '0',
  'start_time': '2022-1-17T11:46:57-0800',
  'end_time': '2022-2-24T11:46:57-0800',
  'campaign_id': 'campaign-id',
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

print(AdAccount(id).create_ad_set(fields=fields, params=params,))

