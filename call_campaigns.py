from facebook_business.adobjects.adaccount import AdAccount
from facebook_business.adobjects.campaign import Campaign
from facebook_business.api import FacebookAdsApi

access_token = 'EAAGbvZAOZBb6ABAMIaOtjQYQ9IMECNF7vjvwXS6BuQtmiYZCWdvQ7V8nsux9mMYZBRPg3VsPf49ahv5Eq1QwnzzwZAuE5y5qJYBLGQ2RneZBxaZBK8jhWLm8EecesAZASqYmNaiktdNvYCmvuDrwKbtuSKhzeNwU5WfpClKDKpMXyu1mYaPJAoUtBX5iqHG0LH4d8CtIZAXPwcA8wq8F7oaWi'
app_secret = 'd71d19dd24ec5e70abc92bbf9fd20856'
app_id = '452713506566048'
id = 'act_4997533496957271'
FacebookAdsApi.init(access_token=access_token)

fields = [
  'name',
  'objective',
]
params = {
  'effective_status': ['PAUSED'],
}
print(AdAccount(id).get_campaigns(fields=fields, params=params,))