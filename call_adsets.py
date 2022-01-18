from facebook_business.adobjects.campaign import Campaign
from facebook_business.adobjects.adset import AdSet
from facebook_business.api import FacebookAdsApi

access_token = 'acces-token'
app_secret = 'app-secret'
app_id = 'app-id'
id = 'ad-account-id'
FacebookAdsApi.init(access_token=access_token)

fields = [
  'name',
  'start_time',
  'end_time',
  'daily_budget',
  'lifetime_budget',
]
params = {
}

print(Campaign(id).get_ad_sets(fields=fields, params=params))
