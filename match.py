import re
from opencc import OpenCC


def is_match(regex, s, trans=True):
    # 支持繁体
    if s and regex:
        if trans:
            try:
                cc = OpenCC("t2s")
                s = cc.convert(s)
                regex = cc.convert(regex)
            except:
                print(regex, s)
        return re.search(regex, s)
    return None

