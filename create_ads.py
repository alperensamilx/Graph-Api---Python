from facebook_business.adobjects.adaccount import AdAccount
from facebook_business.adobjects.ad import Ad
from facebook_business.api import FacebookAdsApi

access_token = '{ACCES-TOKEN}'
app_secret = '{APP-SECRET}'
app_id = '{APP_ID}'
id = '{AD_ACCPUNT_ID}'
FacebookAdsApi.init(access_token=access_token)


def create_ads():
    ad_set_id = str(input('Ad set ID: '))
    name = str(input('Ad Name: '))
    creative_id = str(input('Creative ID: '))
    status = str(input('Status: '))
    print("'since':YYYY-MM-DD,'until':YYYY-MM-DD'")
    time_range = {'since': 2022-1-30, 'until': 2022-2-1}

    fields = [
        'name',
        'preview_shareable_link'
    ]
    params = {
        'name': name,
        'adset_id': ad_set_id,
        'creative': {'creative_id': creative_id},
        'status': status,
    }

    data = AdAccount(id).create_ad(fields=fields, params=params,)
    print(data)


create_ads()


# def create_ads():
#     fields = [
#         'preview_shareable_link'
#     ]
#     params = {
#         'name': 'My Python Ad5',
#         'adset_id': '6290943651216',
#         'creative': {'creative_id': '6291098407816'},
#         'status': 'PAUSED',
#     }
#
#     data = (AdAccount(id).create_ad(fields=fields, params=params,))
#     print(data)
#
#6291340340816
# create_ads()
