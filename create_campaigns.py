from facebook_business.adobjects.adaccount import AdAccount
from facebook_business.adobjects.campaign import Campaign
from facebook_business.api import FacebookAdsApi


access_token = 'acces-token'
app_secret = 'app-secret'
app_id = 'app-id'
id = 'ad-account-id'
FacebookAdsApi.init(access_token=access_token)

fields = [
]
params = {
  'name': 'My Python Campaign',
  'objective': 'PAGE_LIKES',
  'status': 'PAUSED',
  'special_ad_categories': [],
}

print(AdAccount(id).create_campaign(fields=fields, params=params,))

