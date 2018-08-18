from config import Config
from net import NetTool
from history import History
import constants
import match
import download

from bs4 import BeautifulSoup


class Crawl:

    def __init__(self):
        self.config = Config()
        self.net_tool = NetTool()
        self.history = History()


class CrawlDmhy(Crawl):

    def _get_html(self, url):
        return self.net_tool.get(url)

    def _get_torrent(self, page):
        html = self._get_html(constants.DMHY_URL + page).text
        soup = BeautifulSoup(html, 'html.parser')
        a_list = soup.findAll('a')
        for a in a_list:
            try:
                href = a['href']
            except Exception as e:
                pass
            else:
                if match.is_match("\.torrent$", href, trans=False):
                    # 只獲取第一個
                    if not href.startswith("http"):
                        href = "http:" + href
                    return a.string, href
        #             torrent_list.append(href)
        # return torrent_list

    def _search(self, keyword, page_no, preview=False):
        html = self._get_html(constants.DMHY_SEARCH_URL.format(page_no, keyword)).text
        print(constants.DMHY_SEARCH_URL.format(page_no, keyword))
        return self._go(html, preview)

    def _latest(self, page_no, preview=False):
        html = self._get_html(constants.DMHY_PAGE_URL.format(page_no)).text
        return self._go(html, preview)

    def _go(self, html, preview=False):
        # html = self._get_html(constants.DMHY_PAGE_URL.format(page_no)).text
        soup = BeautifulSoup(html, 'html.parser')
        # print(soup)
        title_list = soup.findAll('td', {"class": "title"})
        regex_list = self.config.get_trace_regex_list()
        for title in title_list:
            for c in title.children:
                for regex in regex_list:
                    if c.name == 'a':
                        if match.is_match(regex, c.text, trans=True):
                            title, href = self._get_torrent(c['href'])
                            if preview:
                                print("find: {}, {}".format(title, href))
                            elif not self.history.is_in_history(title):
                                print("start download {}: {}".format(title, href))
                                self.history.save(title)
                                download.download(href)

    def crawl(self, max_page=constants.DEFAULT_LATEST):
        for i in range(1, max_page):
            self._latest(i)

    def preview_crawl(self, max_page=constants.DEFAULT_LATEST):
        for i in range(1, max_page):
            print("page:{}".format(i))
            self._latest(i, preview=True)

    def search(self, key_word, max_page=constants.DEFAULT_SEARCH):
        for i in range(1, max_page):
            self._search(key_word, i)
            print("search page:{}")

    def preview_search(self, key_word, max_page=constants.DEFAULT_SEARCH):
        for i in range(1, max_page):
            print("search page:{}".format(i))
            self._search(key_word, i, preview=True)


if __name__ == '__main__':
    dhmy = CrawlDmhy()
    # dhmy._go(2)
