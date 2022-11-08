import os
import json
from collections import defaultdict

from tomt.benchmarks.gt import GTData, get_documents

import argparse
import numpy as np
import pytrec_eval

from tomt.data import utils

metrics_to_compute = {'recip_rank', 'recall_10', "recall_1"}
parser = argparse.ArgumentParser("create_data_dpr")
parser.add_argument("--root", required=True)
parser.add_argument("--dataset", required=True, choices=("Movies", "Books"))
parser.add_argument("--predictions", required=True)
parser.add_argument("--qas_file", required=False)

if __name__ == '__main__':
    args = parser.parse_args()

    data = GTData(os.path.join(args.root, args.dataset, "splits", "test"))
    queries = data.get_queries()
    qids = [q["id"] for q in queries]
    qrels = data.get_qrels(True)

    with open(args.predictions, "r") as reader:
        predictions = json.load(reader)

    assert all([qid in predictions for qid in qids])

    evaluator = pytrec_eval.RelevanceEvaluator(qrels, metrics_to_compute)

    acc_metrics = defaultdict(list)
    for qid, res in evaluator.evaluate(predictions).items():
        for met in metrics_to_compute:
            acc_metrics[met].append((qid, res[met]))

    mean_metrics = {}

    for met, all_vals in sorted(acc_metrics.items(), key=lambda _: _[0]):
        vals = [val for (qid, val) in all_vals]
        mean_metrics[met] = {
            "mean": np.mean(vals),
            "std": np.std(vals)
        }
        print(f"{met}: {round(np.mean(vals), 4)}, ({round(np.std(vals), 4)})")
