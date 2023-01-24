import os
import argparse
import time
import logging
from config import configure_logging
from tomt.data import utils, reddit
from tqdm import tqdm

log = logging.getLogger(__name__)


def get_data(submission_id, cache_dir, reddit_config, force_refresh=False, get_comments=False):
    p = os.path.join(cache_dir, submission_id + ".pkl")
    # load from cache
    if force_refresh or not os.path.exists(p):
        submission = reddit.get_submission(submission_id, reddit_config, get_comments)
        if submission is None:
            raise ValueError("not found!")

        utils.write_pickle(submission, p)
        return submission
    else:
        return utils.load_pickle(p)


def load_fields(data, cache_dir, reddit_config_path, force_refresh):
    reddit_config = utils.read_json(reddit_config_path)
    not_found = 0
    for d in tqdm(data, unit="doc"):
        try:
            submission = get_data(d["id"], cache_dir,
                                  reddit_config=reddit_config,
                                  force_refresh=force_refresh,
                                  get_comments=False)
        except:
            not_found += 1
            continue
        # todo: clean?
        d["title"] = submission.title
        d["description"] = submission.selftext

    log.info(f"not found: {not_found}")


if __name__ == '__main__':
    parser = argparse.ArgumentParser("process_dataset")
    parser.add_argument("--input", help="location to input .json file", required=True)
    parser.add_argument("--out", help="location to output .json file", required=True)
    parser.add_argument("--cache", help="directory to cache data", default="./.submissions_cache")
    parser.add_argument("--force_refresh", action="store_true", default=False)
    parser.add_argument(
        "--reddit_config_path", help="location of reddit config", default="./reddit_config.json")
    configure_logging("CreateFiles", False)

    args = parser.parse_args()
    log.info(f"args: {args}")
    assert args.input != args.out, "input == out!"
    os.makedirs(args.cache, exist_ok=True)
    start_time = time.time()
    data = utils.read_jsonl(args.input)
    load_fields(data, args.cache, args.reddit_config_path, args.force_refresh)
    utils.write_jsonl(data, args.out)
    log.info(f"took {time.time() - start_time} seconds!")
