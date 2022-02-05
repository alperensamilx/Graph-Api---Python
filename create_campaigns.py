from facebook_business.adobjects.adaccount import AdAccount
from facebook_business.adobjects.campaign import Campaign
from facebook_business.api import FacebookAdsApi


access_token = 'acces-token'
app_secret = 'app-secret'
app_id = 'app-id'
id = 'ad-account-id'
FacebookAdsApi.init(access_token=access_token)

def create_campaigns():
    name = str(input('Campaign Name: '))
    print('NONE, EMPLOYMENT, HOUSING, CREDIT, ISSUES_ELECTIONS_POLITICS, ONLINE_GAMBLING_AND_GAMING')
    special_ad_categories = (input('Special Ad Categories: '))
    print('Use one of: APP_INSTALLS, BRAND_AWARENESS, EVENT_RESPONSES, LEAD_GENERATION, LINK_CLICKS, LOCAL_AWARENESS, MESSAGES, OFFER_CLAIMS, PAGE_LIKES, POST_ENGAGEMENT, PRODUCT_CATALOG_SALES, REACH, STORE_VISITS, VIDEO_VIEWS, CONVERSIONS.')
    objective = str(input('Campaign objective: '))
    print('PAUSED')
    status = str(input('Status: '))


    fields = [
        'name',
    ]
    params = {
        'name': name,
        'objective': objective,
        'status': status,
        'special_ad_categories': special_ad_categories,
    }

    data = (AdAccount(id).create_campaign(fields=fields, params=params))
    print(data)

