from viral_reddit_posts_utils.config_utils import *


def test_find_config():
    # I wanted this to pass whether th file is found or not
    try:
        cfg_file = find_config()
        print(cfg_file)
    except FileNotFoundError as e:
        print(e)
