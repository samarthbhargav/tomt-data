import os
import re
import json
from tomt.benchmarks.gt import GTData, get_documents
root = "/data/TOMT"
dataset = "Movies"

# save data for DPR
file_path = "/data/TOMT/Movies/DPR/"

documents = get_documents(os.path.join(root, dataset), hard_negatives=True, negatives=True)

id2doc = dict()
for record in documents:
    _input = re.sub(r"(?<![A-Z][a-z])([!?.])(?=\s*[A-Z])\s*", r"\1\n", record['text'])
    id2doc[record["id"]]= {"title":record["id"], "text":record['text'], "sents":_input.split("\n")}

with open(file_path+'id2doc2.json', 'w') as f:
    json.dump(id2doc, f, ensure_ascii=False,indent=4)

