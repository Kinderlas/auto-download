import os
from pathlib import Path

config_path = "./config.ini"
REGEX = "regex"
TIME_INTERVAL = "time"
DEFAULT_SESSION = "trace"
DMHY_URL = "https://share.dmhy.org/"
DMHY_PAGE_URL = "https://share.dmhy.org/topics/list/page/{}"
DMHY_SEARCH_URL = "https://share.dmhy.org/topics/list/page/{}?keyword={}"
TEMP_PATH = "/tmp/auto-download/"
HOME_PATH = str(Path.home())
HISTORY_PATH = HOME_PATH + "/.auto-download/"
HISTORY_FILE = HISTORY_PATH + "history.log"
OUT_PATH = HOME_PATH + "/Downloads/auto"
DEFAULT_LATEST = 6
DEFAULT_SEARCH = 4

if not os.path.exists(TEMP_PATH):
    os.mkdir(TEMP_PATH)

if not os.path.exists(OUT_PATH):
    os.mkdir(OUT_PATH)

if not os.path.exists(HISTORY_PATH):
    os.mkdir(HISTORY_PATH)
