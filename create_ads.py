from facebook_business.adobjects.adaccount import AdAccount
from facebook_business.adobjects.ad import Ad
from facebook_business.api import FacebookAdsApi

access_token = 'acces-token'
app_secret = 'app-secret'
app_id = 'app-id'
id = 'ad-account-id'
FacebookAdsApi.init(access_token=access_token)

fields = [
]
params = {
  'name': 'My Python Ad',
  'adset_id': 'ad-set-id',
  'creative': {'creative_id': 'creative-id'},
  'status': 'PAUSED',
}

print(AdAccount(id).create_ad(fields=fields,params=params,))


