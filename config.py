import configparser
import constants
from ast import literal_eval


class Config:

    def __init__(self, path=None, session=constants.DEFAULT_SESSION):
        if not path:
            path = constants.config_path
        self.session = session
        self._cf = configparser.RawConfigParser()
        self._cf.read(path)

    def get_trace_regex_list(self):
        return literal_eval(self._cf.get(self.session, constants.REGEX))

    def get_time_interval(self):
        return self._cf.get(self.session, constants.TIME_INTERVAL)


if __name__ == '__main__':
    config = Config()
    print(config.get_time_interval())
    print(config.get_trace_regex_list())
