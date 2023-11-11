def assetDetails():
    import json
    from config import details
    path = open(details())
    data = json.load(path)
    num_assets = len(data)
    # num_assets = 1

    included_terms = [
            "name",
            "id",
            "preview",
            "type"
        ]

    asset_lst = []

    for assets in range(num_assets):
        att_lst = []
        for attribute in range(len(included_terms)):
            att_lst.append(data[assets][included_terms[attribute]])
        asset_lst.append(att_lst)
    return asset_lst