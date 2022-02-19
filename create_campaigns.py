from facebook_business.adobjects.adaccount import AdAccount
from facebook_business.adobjects.campaign import Campaign
from facebook_business.api import FacebookAdsApi


access_token = 'acces-token'
app_secret = 'app-secret'
app_id = 'app-id'
id = 'ad-account-id'
FacebookAdsApi.init(access_token=access_token)

# Creating Campaign
def create_campaign():
    special_ad_categories_list = ['NONE', 'EMPLOYMENT', 'HOUSING', 'CREDIT', 'ISSUES_ELECTIONS_POLITICS', 'ONLINE_GAMBLING_AND_GAMING']
    campaign_objective_list = ['APP_INSTALLS', 'BRAND_AWARENESS', 'EVENT_RESPONSES', 'LEAD_GENERATION', 'LINK_CLICKS', 'LOCAL_AWARENESS', 'MESSAGES', 'OFFER_CLAIMS', 'PAGE_LIKES', 'POST_ENGAGEMENT', 'PRODUCT_CATALOG_SALES', 'REACH', 'STORE_VISITS', 'VIDEO_VIEWS', 'CONVERSIONS']
    status_list = ['ACTIVE', 'PAUSED']
    name = input('Campaign Name: ')
    print('Use coma. NONE, EMPLOYMENT, HOUSING, CREDIT, ISSUES_ELECTIONS_POLITICS, ONLINE_GAMBLING_AND_GAMING')
    while True:
        x = input('Special Ad Categories: ').upper().split(',')
        if x in special_ad_categories_list:
            special_ad_categories = x
            break
        else:
            print('Use one of: NONE, EMPLOYMENT, HOUSING, CREDIT, ISSUES_ELECTIONS_POLITICS, ONLINE_GAMBLING_AND_GAMING]')
    print('Use one of: APP_INSTALLS, BRAND_AWARENESS, EVENT_RESPONSES, LEAD_GENERATION, LINK_CLICKS, LOCAL_AWARENESS, MESSAGES, OFFER_CLAIMS, PAGE_LIKES, POST_ENGAGEMENT, PRODUCT_CATALOG_SALES, REACH, STORE_VISITS, VIDEO_VIEWS, CONVERSIONS.')
    while True:
        x = input('Campaign objective: ').upper()
        if x in campaign_objective_list:
            objective = x
            break
        else:
            print('Use one of: APP_INSTALLS, BRAND_AWARENESS, EVENT_RESPONSES, LEAD_GENERATION, LINK_CLICKS, LOCAL_AWARENESS, MESSAGES, OFFER_CLAIMS, PAGE_LIKES, POST_ENGAGEMENT, PRODUCT_CATALOG_SALES, REACH, STORE_VISITS, VIDEO_VIEWS, CONVERSIONS.')

    print('Use one of: ACTIVE, PAUSED')
    while True:
        x = input('Status: ').upper()
        if x in status_list:
            status = x
            break
        else:
            print('Use one of: ACTIVE, PAUSED')


    fields = [
        'name',
    ]


    params = {
        'name': name,
        'objective': objective,
        'status': status,
        'special_ad_categories': special_ad_categories,
    }

    data = AdAccount(id).create_campaign(fields=fields, params=params)
    print(data)
