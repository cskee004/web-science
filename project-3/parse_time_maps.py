import json 
import os
import pandas as pd
from collections import defaultdict

results = defaultdict(int)

def parse_maps():
    zero_count = 0
    for name in os.listdir(r"./time-maps"):
        file_path = os.path.join(r"./time-maps", name)
        file_size = os.path.getsize(file_path)
        if file_size > 0:
            temp_list = []
            with open(file_path, encoding='utf-8') as f:
                data = json.load(f)
                for i in data['mementos']['list']:
                    temp_list.append(i)
            num_mementos = len(temp_list)
            results[num_mementos] += 1
        else:
            zero_count += 1
    results[0] = zero_count
    keys = list(results.keys())
    keys.sort()
    sorted_results = {i: results[i] for i in keys}
    return sorted_results
    

def bin_results(d):
    keys_dict = list(d.keys()) 
    value_dict = list(d.values())
    ds = pd.Series(keys_dict)
    bd = pd.qcut(ds, q=15, labels=False)
    bin_list = bd.to_list() 
    merged_zip = zip(bin_list, zip(keys_dict, value_dict))
    merged_list = list(merged_zip)
    with open('./merged-list.txt', 'w') as f:
        for item in merged_list:
            f.write(str(item) + '\n')
    return merged_list

sorted_results = parse_maps()
merged_list = bin_results(sorted_results)



