from facebook_business.adobjects.adaccount import AdAccount
from facebook_business.adobjects.campaign import Campaign
from facebook_business.api import FacebookAdsApi


access_token = 'EAAGbvZAOZBb6ABANr2iam1UYZA6LZAFUKDRVzvnt1G11Nc3VZAigrIXQfdvcKsFiv7SSYwwMuTH6bUFKpbfXa0BqsX3W0ogClZAJpqWNIDtHRx2jZB6vU7iIdIqcJkfAadet0lm8YVLaqMLwLNHVXhnq48jnbmcDMaRSZBj7ZBzNiTLTWFHuPZCLtZCLKAeqDwqAAApvRDtEqiGM5BLIeBnZCOZAH'
app_secret = 'd71d19dd24ec5e70abc92bbf9fd20856'
app_id = '452713506566048'
id = 'act_4997533496957271'
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
