import os
import json
from tomt.benchmarks.gt import GTData, get_documents
root = "/data/TOMT"
dataset = "Movies"

# save data for DPR
file_path = "/data/TOMT/Movies/"

documents = get_documents(os.path.join(root, dataset), hard_negatives=True, negatives=True)
split = "test"
gtdata = GTData(os.path.join(root, dataset, "splits", split))
data = gtdata.get_grouped_data(os.path.join(root, dataset), "all",hn_source="tomt_hn")


with open(file_path+'qas_test.json', 'w') as f:
    for record in data:
        f.write(json.dumps({'_id':record["query"]["id"],
                            'answer':[record["positive_documents"][0]["title"]],
                            'question':record["query"]["description"],
                            'sp':[i["id"] for i in record["positive_documents"]],
                           }))
        f.write('\n')

