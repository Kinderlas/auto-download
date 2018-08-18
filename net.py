import requests
import constants


class NetTool:

    def __init__(self, use_proxy=True):

        if use_proxy:
            self.proxies = {
                "http": "socks5://127.0.0.1:1080",
                'https': 'socks5://127.0.0.1:1080'
            }
        else:
            self.proxies = None

    def get(self, url):
        return requests.get(url, proxies=self.proxies)


if __name__ == '__main__':
    t = NetTool(False)
    r = t.get(constants.DMHY_URL)
    print(r.text)
