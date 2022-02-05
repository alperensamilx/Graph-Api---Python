from facebook_business.adobjects.adaccount import AdAccount
from facebook_business.adobjects.campaign import Campaign
from facebook_business.api import FacebookAdsApi

access_token = '{ACCES-TOKEN}'
app_secret = '{APP-SECRET}'
app_id = '{APP_ID}'
id = '{AD_ACCPUNT_ID}'
FacebookAdsApi.init(access_token=access_token)


def call_campaigns():
    fields = [
      'name',
      'objective',
    ]
    params = {
      'effective_status': ['PAUSED'],
    }
    return AdAccount(id).get_campaigns(fields=fields, params=params,)


response = call_campaigns()
print(response)


def campaign_csv():
    count = len(response)
    with open('campaigns2.csv', 'w', newline='') as f:
        fieldnames = ['id', 'name', 'objective']
        the_writer = csv.DictWriter(f, fieldnames=fieldnames)

        the_writer.writeheader()
        for i in range(count):
            the_writer.writerow({'id': response[i]['id'], 'name': response[i]['name'], 'objective': response[i]['objective']})


campaign_csv()
