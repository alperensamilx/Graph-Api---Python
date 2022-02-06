from facebook_business.adobjects.adaccount import AdAccount
from facebook_business.adobjects.campaign import Campaign
from facebook_business.api import FacebookAdsApi
import json
import csv


FacebookAdsApi.init(access_token=access_token)


def call_ads():
    fields = [
        'name',
        'adset_id',
        'campaign_id',
        'creative',
        'preview_shareable_link',
        # 'tracking_specs',



    ]
    params = {
        'effective_status': ['PAUSED'],


    }
    return AdAccount(id).get_ads(fields=fields, params=params,)


response = call_ads()
print(response)


def ad_csv():
    count = len(response)
    with open('ad.csv', 'w', newline='') as f:
        fieldnames = ['id', 'name', 'adset_id', 'preview_shareable_link']
        the_writer = csv.DictWriter(f, fieldnames=fieldnames)

        the_writer.writeheader()
        for i in range(count):
            the_writer.writerow({'id': response[i]['id'], 'name': response[i]['name'], 'adset_id': response[i]['adset_id'], 'preview_shareable_link': response[i]['preview_shareable_link']})


# ad_csv()


def ad_ab_csv():
    count = len(response)
    with open('ad.csv', 'w', newline='') as f:
        fieldnames = ['ad_id', 'campaign_id', 'adset_id']
        the_writer = csv.DictWriter(f, fieldnames=fieldnames)

        the_writer.writeheader()
        for i in range(count):
            the_writer.writerow({'ad_id': response[i]['id'], 'campaign_id': response[i]['campaign_id'], 'adset_id': response[i]['adset_id']})


# ad_ab_csv()