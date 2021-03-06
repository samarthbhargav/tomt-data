import os
import json
from tomt.benchmarks.gt import GTData, get_documents
root = "/data/TOMT"
dataset = "Movies"

# save data for DPR
file_path = "/data/TOMT/Movies/DPR/"

documents = get_documents(os.path.join(root, dataset), hard_negatives=True, negatives=True)
for split in ["test", "train", "validation"]:
    gtdata = GTData(os.path.join(root, dataset, "splits", split))
    data = gtdata.get_grouped_data(os.path.join(root, dataset), "all", hn_source="tomt_hn") #(os.path.join(root, dataset), "all")
    #print(data[0]) # <--- one training point


    with open(file_path+split+"_dpr.json", 'w') as f:
        for record in data:
            neg_records = []
            for neg_record in record["bm25_hn_negatives"]:#record["bm25_negatives"]:
               if len(neg_record["text"].split())<1:
                   neg_records.append({"title":neg_record["id"],"text":neg_record["title"]})
               else:
                   neg_records.append({"title":neg_record["id"],"text":neg_record["text"]})
            pos_records = []
            for pos_record in record["positive_documents"]:
               pos_records.append({"title":pos_record["id"],"text":pos_record["text"]})
            f.write(json.dumps({'_id':record["query"]["id"],'question': record["query"]["description"],
                               'neg_paras':neg_records,'pos_paras':pos_records,
                               'answers': [record["positive_documents"][0]["title"]]}))
            f.write('\n')

