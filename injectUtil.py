from sqlInject import inject
from sqlCheck import check_spec_id
import json
import parse
from config import details

parse_lst = parse.assetDetails()

path = open(details())
data = json.load(path)
num_assets = len(data)

for assetInject in range(num_assets):
    crnt_asset = parse_lst[assetInject]
    crnt_id = crnt_asset[1]
    if check_spec_id(crnt_id) == False:
        inject(crnt_asset)