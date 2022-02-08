access_token = '{ACCES-TOKEN}'
app_secret = '{APP-SECRET}'
app_id = '{APP_ID}'
id = '{AD_ACCPUNT_ID}'
FacebookAdsApi.init(access_token=access_token)


# Ad Creative
def call_ad_creative():


    fields = [
        'name',
        'image_hash'
    ]

    params = {
    }
    data = AdAccount(id).get_ad_creatives(fields=fields, params=params)
    print(data)


call_ad_creative()

