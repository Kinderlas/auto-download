import configparser
from constants import config_path
from ast import literal_eval


class Config:

    def __init__(self, path=None):
        if not path:
            path = config_path
        self._cf = configparser.RawConfigParser()
        self._cf.read(path)

    def get_trace_regex_list(self):
        return literal_eval(self._cf.get("trace", "regex"))

    def get_time_interval(self):
        return self._cf.get("trace", "time")


if __name__ == '__main__':
    config = Config()
    print(config.get_time_interval())
    print(config.get_trace_regex_list())
