


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

