from config import details
import json
import os
path = open(details())
# data = json.load(path)
# data_len = len(data)
# add_path = "F:\\Custom\\Downloaded\\"
# for ids in range(data_len):
#     path_lst = data[ids]['preview']
#     bse_str = ''
#     for prev_path in range(3):
#         if prev_path != 2:
#             bse_str = bse_str + path_lst[prev_path] + "\\"
#         else:
#             bse_str = bse_str + path_lst[prev_path]
#     bse_str = add_path + bse_str
#     print(bse_str)
    
def parseByTerm(term:str, path:str):
    data = json.load(path)
    data_len = len(data)
    for ids in range(data_len):
        prin_term_srch = data[ids][term]
    return prin_term_srch
        
parseByTerm("name", path)

def sql_prep():
    included_terms = [
        "name",
        "id",
        "preview",
        "type"
    ]
    
    mul_asset_detail_lst = []
    for json_query in range(len(included_terms)):
        asset_det = []
        asset_det.append(parseByTerm(included_terms[json_query], open("F:\\Custom\\Downloaded\\assetsData.json")))
        mul_asset_detail_lst.append(asset_det)
    return mul_asset_detail_lst

print(sql_prep())