from facebook_business.adobjects.adaccount import AdAccount
from facebook_business.adobjects.campaign import Campaign
from facebook_business.api import FacebookAdsApi

access_token = 'acces-token'
app_secret = 'app-secret'
app_id = 'app-id'
id = 'ad-account-id'
FacebookAdsApi.init(access_token=access_token)

fields = [
  'name',
  'objective',
]
params = {
  'effective_status': ['PAUSED'],
}
print(AdAccount(id).get_campaigns(fields=fields, params=params,))
