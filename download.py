from urllib.request import urlretrieve
import constants
import os
from xmlrpc import client


def submit_task_to_aria(torrent_path):
    server = client.ServerProxy('http://localhost:6800/rpc', allow_none=True)
    server.aria2.addTorrent(client.Binary(open(torrent_path, 'rb').read()))  # , uris, options, position)


def download_torrent_file(url, save_name=None):
    if not save_name:
        save_name = os.path.basename(url)
    save_name = constants.TEMP_PATH + save_name
    urlretrieve(url, save_name)
    print(save_name)
    return save_name


def download(url):
    submit_task_to_aria(download_torrent_file(url))


if __name__ == '__main__':
    download(download_torrent_file("http://dl.dmhy.org/2018/08/18/1e75a32d9e639ef513c281da1f9c828e7fd864ec.torrent"))
