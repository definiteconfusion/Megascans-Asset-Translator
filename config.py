def details():
    import json
    path = open('config.json')
    data = json.load(path)
    assetsPath = data['assetsPath']
    return assetsPath