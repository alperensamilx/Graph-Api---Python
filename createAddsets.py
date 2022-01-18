from facebook_business.adobjects.adaccount import AdAccount
from facebook_business.adobjects.adset import AdSet
from facebook_business.api import FacebookAdsApi

access_token = 'EAAGbvZAOZBb6ABANr2iam1UYZA6LZAFUKDRVzvnt1G11Nc3VZAigrIXQfdvcKsFiv7SSYwwMuTH6bUFKpbfXa0BqsX3W0ogClZAJpqWNIDtHRx2jZB6vU7iIdIqcJkfAadet0lm8YVLaqMLwLNHVXhnq48jnbmcDMaRSZBj7ZBzNiTLTWFHuPZCLtZCLKAeqDwqAAApvRDtEqiGM5BLIeBnZCOZAH'
app_secret = 'd71d19dd24ec5e70abc92bbf9fd20856'
app_id = '452713506566048'
id = 'act_4997533496957271'
FacebookAdsApi.init(access_token=access_token)

fields = [
]
params = {
  'name': 'My Python AdSet',
  'lifetime_budget': '0',
  'start_time': '2022-1-17T11:46:57-0800',
  'end_time': '2022-2-24T11:46:57-0800',
  'campaign_id': '23849368774560502',
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

