import constants
import datetime
import os


class History:

    def __init__(self, history_file=constants.HISTORY_FILE):
        self._history = set()
        self._history_file = history_file

    def load_history(self):
        self._history.clear()
        if os.path.exists(self._history_file):
            with open(self._history_file, 'r') as f:
                for row in f:
                    try:
                        self._history.add(row.split("::")[0])
                    except:
                        pass

    def save(self, title):
        self._history.add(title)
        with open(constants.HISTORY_FILE, 'a') as f:
            f.write(title + "::" + datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
            f.write("\n")

    def is_in_history(self, title):
        if not self._history:
            self.load_history()
        return title in self._history

    def reset_history(self):
        if os.path.exists(self._history_file):
            os.remove(self._history_file)


if __name__ == '__main__':
    h = History()
    h.reset_history()
    h.save("lalala")
    h.save("banana")
    print(h.is_in_history("banana"))
    h2 = History()
    print(h2.is_in_history("banana"))
