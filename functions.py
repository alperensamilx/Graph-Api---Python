from facebook_business.adobjects.adaccount import AdAccount
from facebook_business.adobjects.campaign import Campaign
from facebook_business.adobjects.page import Page

from facebook_business.api import FacebookAdsApi

import csv

access_token = '{ACCES-TOKEN}'
app_secret = '{APP-SECRET}'
app_id = '{APP_ID}'
id = '{AD_ACCPUNT_ID}'
FacebookAdsApi.init(access_token=access_token)

# Creating Campaign
def create_campaign():
    name = str(input('Campaign Name: '))
    print('NONE, EMPLOYMENT, HOUSING, CREDIT, ISSUES_ELECTIONS_POLITICS, ONLINE_GAMBLING_AND_GAMING')
    special_ad_categories = str(input('Special Ad Categories: '))
    print(
        'Use one of: APP_INSTALLS, BRAND_AWARENESS, EVENT_RESPONSES, LEAD_GENERATION, LINK_CLICKS, LOCAL_AWARENESS, MESSAGES, OFFER_CLAIMS, PAGE_LIKES, POST_ENGAGEMENT, PRODUCT_CATALOG_SALES, REACH, STORE_VISITS, VIDEO_VIEWS, CONVERSIONS.')
    objective = str(input('Campaign objective: ')).upper()
    print('PAUSED')
    status = str(input('Status: ')).upper()

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


# Creating Ad Set
def create_ad_set():
    campaign_id = str(input('Campaign ID: '))
    name = str(input('Ad set name: '))

    print('Budget & schedule')
    print('52500')
    lifetime_budget = str(input('Lifetime Budget: '))
    print('YYYY-MM-DDTHH:MM:SS')
    start_time = str(input('Start Date: '))
    print('YYYY-MM-DDTHH:MM:SS')
    end_time = str(input('End Date: '))

    print('Audience')
    age_min = str(input('Age Min: '))
    age_max = str(input('Age Max: '))

    print('Optimization & delivery')
    print('{NONE, APP_INSTALLS, AD_RECALL_LIFT, ENGAGED_USERS, EVENT_RESPONSES, IMPRESSIONS, LEAD_GENERATION, QUALITY_LEAD, LINK_CLICKS, OFFSITE_CONVERSIONS, PAGE_LIKES, POST_ENGAGEMENT, QUALITY_CALL, REACH, LANDING_PAGE_VIEWS, VISIT_INSTAGRAM_PROFILE, VALUE, THRUPLAY, DERIVED_EVENTS, APP_INSTALLS_AND_OFFSITE_CONVERSIONS, CONVERSATIONS, IN_APP_VALUE}')
    optimization_goal = str(input('Optimization for ad delivery: ')).upper()
    print('1370')
    bid_amount = str(input('Bid control (optional): '))
    print('PAUSED')
    status = str(input('Status: ')).upper()

    fields = [
        'name',
    ]
    params = {
        'name': name,
        'lifetime_budget': lifetime_budget,
        'start_time': start_time,
        'end_time': end_time,
        'campaign_id': campaign_id,
        'bid_amount': bid_amount,
        'billing_event': 'IMPRESSIONS',
        'optimization_goal': optimization_goal,
        'targeting': {
            'age_min': age_min,
            'age_max': age_max,
            'behaviors': [{'id': 6002714895372, 'name': 'All travelers'}],
            'genders': [1],
            'geo_locations': {'countries': ['US'],
                              'regions': [{'key': '4081'}],
                              'cities': [{'key': '777934', 'radius': 10, 'distance_unit': 'mile'}]},
            'interests': [{'id': '6003139266461', 'name': 'Movies'}],
            'life_events': [{'id': 6002714398172, 'name': 'Newlywed (1 year)'}],
            'facebook_positions': ['feed'],
            'publisher_platforms': ['facebook', 'audience_network']},
        'status': status,
    }

    data = AdAccount(id).create_ad_set(fields=fields, params=params)
    print(data)


# Ad Creative
def ad_creative():
    name = str(input('Creative Name: '))
    print('103122378948499')
    page_id = str(input('Page ID: '))
    image_hash = str(input('Image Hash: '))
    website_url = str(input('Website URL: '))
    primary_text = str(input('Primary text: '))
    headline = str(input('Headline: '))
    description = str(input('Description: '))
    print('LEARN_MORE')
    call_to_action = str(input("Call to Action: ")).upper()

    fields = [
        'name',
    ]

    params = {
        'name': name,
        'object_story_spec': {'page_id': page_id,
                              'link_data': {
                                  'image_hash': image_hash,
                                  'link': website_url,
                                  'message': primary_text,
                                  'name': headline,
                                  "description": description,
                                  "call_to_action": {
                                      "type": call_to_action
                                  }

                              }},
    }
    data = AdAccount(id).create_ad_creative(fields=fields, params=params)
    print(data)


# Creating Ad
def create_ad():
    adset_id = str(input('Ad Set ID: '))
    name = str(input('Ad Name: '))
    creative_id = str(input('Creative ID: '))
    status = str(input('Status: ')).upper()
    print("'since':YYYY-MM-DD,'until':YYYY-MM-DD'")

    fields = [
        'name',
        'preview_shareable_link',

    ]
    params = {
        'name': name,
        'adset_id': adset_id,
        'creative': {'creative_id': creative_id},
        'status': status,
    }

    data = AdAccount(id).create_ad(fields=fields, params=params)
    print(data)


# Calling Campaign
def call_campaigns():
    fields = [
      'name',
      'objective',
    ]
    params = {
      'effective_status': ['PAUSED'],
    }
    return AdAccount(id).get_campaigns(fields=fields, params=params)


response_campaigns = call_campaigns()


def campaign_csv():
    count = len(response_campaigns)
    with open('campaigns.csv', 'w', newline='') as f:
        fieldnames = ['id', 'name', 'objective']
        the_writer = csv.DictWriter(f, fieldnames=fieldnames)

        the_writer.writeheader()
        for i in range(count):
            the_writer.writerow({'id': response_campaigns[i]['id'], 'name': response_campaigns[i]['name'], 'objective': response_campaigns[i]['objective']})


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
        'delivery_estimate',
    ]

    params = {}

    return Campaign(id).get_ad_sets(fields=fields, params=params)


response_ad_sets = call_ad_sets()


def ad_set_csv():
    count = len(response_ad_sets)
    with open('ad_sets.csv', 'w', newline='') as f:
        fieldnames = ['campaign_id', 'id', 'name', 'start_time', 'end_time', 'daily_budget', 'lifetime_budget', 'optimization_goal']
        the_writer = csv.DictWriter(f, fieldnames=fieldnames)

        the_writer.writeheader()
        for i in range(count):
            the_writer.writerow({'campaign_id': response_ad_sets[i]['campaign_id'], 'id': response_ad_sets[i]['id'], 'name': response_ad_sets[i]['name'], 'start_time': response_ad_sets[i]['start_time'], 'end_time': response_ad_sets[i]['end_time'], 'lifetime_budget': response_ad_sets[i]['lifetime_budget'], 'daily_budget': response_ad_sets[i]['daily_budget'], 'optimization_goal': response_ad_sets[i]['optimization_goal']})


# Calling ads
def call_ads():
    fields = [
        'name',
        'adset_id',
        'creative',
        'preview_shareable_link',
        'tracking_specs',
        'bid_amount',



    ]
    params = {
      'effective_status': ['PAUSED'],
    }
    return AdAccount(id).get_ads(fields=fields, params=params)


response_ads = call_ads()


def ad_csv():
    count = len(response_ads)
    with open('ads.csv', 'w', newline='') as f:
        fieldnames = ['id', 'name', 'adset_id', 'preview_shareable_link']
        the_writer = csv.DictWriter(f, fieldnames=fieldnames)

        the_writer.writeheader()
        for i in range(count):
            the_writer.writerow({'id': response_ads[i]['id'], 'name': response_ads[i]['name'], 'adset_id': response_ads[i]['adset_id'], 'preview_shareable_link': response_ads[i]['preview_shareable_link']})


def call_ad_creative():

    fields = [
        'name',
        'image_hash'
    ]

    params = {
    }
    data = AdAccount(id).get_ad_creatives(fields=fields, params=params)
    return data




def create_video():
    print('103122378948499')
    page_id = str(input("Page ID: "))
    print('https://scontent.fist4-1.fna.fbcdn.net/v/t1.18169-9/11701119_1096804877014160_4246085576298344409_n.jpg?_nc_cat=111&ccb=1-5&_nc_sid=09cbfe&_nc_ohc=RU_deGQrNEkAX9KwO2B&_nc_ht=scontent.fist4-1.fna&oh=00_AT-NqO6aiivQOOQ6eyzi9ShJmQqLh51BAUc-ABfyYPo5yQ&oe=62150B12')
    image_url = str(input("Image URL: "))
    print('5167895076567743')
    video_id = str(input('Video ID: '))
    print('LIKE_PAGE')
    call_to_action = str(input("Call to Action: ")).upper()

    fields = [
    ]
    params = {
        'name': 'Video Creative',

        'object_story_spec': {'page_id': page_id,
                              'video_data': {
                                          'image_url': image_url,
                                          'video_id': video_id,
                                          'call_to_action': {'type': call_to_action, 'value': {'page': page_id}}
                                            },


                              },
    }
    data = AdAccount(id).create_ad_creative(fields=fields, params=params)
    print(data)


def create_carousel():
      fields = [
      ]

      params = {
        'message': 'Browse our latest products',
        'published': '0',
        'child_attachments': [{
          'link': '<link>',
          'name': 'Product 1',
          'description': '$4.99',
          'image_hash': '<imageHash>'
        },
          {
            'link': '<link>',
            'name': 'Product 2',
            'description': '$4.99',
            'image_hash': '<imageHash>'
          },
          {
            'link': '<link>',
            'name': 'Product 3',
            'description': '$4.99',
            'image_hash': '<imageHash>'
          },
          {
            'link': '<link>',
            'name': 'Product 4',
            'description': '$4.99',
            'image_hash': '<imageHash>'
          },
        ],
        'caption': 'WWW.EXAMPLE.COM',
        'link': 'http://www.example.com/products',
      }

      data = Page(id).get_posts(fields=fields, params=params)
      print(data)

