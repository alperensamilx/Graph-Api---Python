from facebook_business.adobjects.campaign import Campaign
from facebook_business.adobjects.adset import AdSet
from facebook_business.api import FacebookAdsApi

access_token = '{ACCES-TOKEN}'
app_secret = '{APP-SECRET}'
app_id = '{APP_ID}'
id = '{AD_ACCPUNT_ID}'
FacebookAdsApi.init(access_token=access_token)

# Calling Ad Set
def call_ad_sets():
    fields = [
        'campaign_id',
        'id',
        'name',
        'start_time',
        'end_time',
        'daily_budget',
        'lifetime_budget',
        'optimization_goal',
        'targeting',
        # 'delivery_estimate',
    ]

    params = {}

    return Campaign(id).get_ad_sets(fields=fields, params=params)


response_ad_sets = call_ad_sets()
print(response_ad_sets)


def ad_set_csv():
    count = len(response_ad_sets)
    with open('ad_sets_targeting.csv', 'w', newline='') as f:
        fieldnames = ['campaign_id', 'id', 'name', 'start_time', 'end_time', 'daily_budget', 'lifetime_budget', 'optimization_goal']
        the_writer = csv.DictWriter(f, fieldnames=fieldnames)

        the_writer.writeheader()
        for i in range(count):
            the_writer.writerow({'campaign_id': response_ad_sets[i]['campaign_id'], 'id': response_ad_sets[i]['id'], 'name': response_ad_sets[i]['name'], 'start_time': response_ad_sets[i]['start_time'], 'end_time': response_ad_sets[i]['end_time'], 'lifetime_budget': response_ad_sets[i]['lifetime_budget'], 'daily_budget': response_ad_sets[i]['daily_budget'], 'optimization_goal': response_ad_sets[i]['optimization_goal']})


def ad_set_targeting():
    count = len(response_ad_sets)
    with open('ad_sets_targeting.csv', 'w', newline='') as f:
        fieldnames = ['id', 'name', 'age_max', 'age_min', 'genders', 'behaviors', 'life_events', 'interests', 'publisher_platforms']
        the_writer = csv.DictWriter(f, fieldnames=fieldnames)
        the_writer.writeheader()
        for i in range(count):
            the_writer.writerow({'id': response_ad_sets[i]['id'], 'name': response_ad_sets[i]['name'], 'age_max': response_ad_sets[i]['targeting']['age_max'], 'age_min': response_ad_sets[i]['targeting']['age_min'], 'genders': response_ad_sets[i]['targeting']['genders'][0], 'behaviors': response_ad_sets[i]['targeting']['behaviors'][0]['name'], 'life_events': response_ad_sets[i]['targeting']['life_events'][0]['name']})


ad_set_targeting()


def ad_set_delivery_estimate():
    count = len(response_ad_sets)
    with open('ad_sets_delivery.csv', 'w', newline='') as f:
        fieldnames = ['delivery_estimate']
        the_writer = csv.DictWriter(f, fieldnames=fieldnames)
        the_writer.writeheader()
        for i in range(count):
            the_writer.writerow({'delivery_estimate': response_ad_sets[i]['delivery_estimate']['data'][0]['daily_outcomes_curve']})


# ad_set_delivery_estimate()
