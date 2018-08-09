import json
import re


class Parse:
    def __init__(self):
        self.url_pattern = {
            'scheme': None,
            'user': None,
            'pass': None,
            'host': None,
            'port': None,
            'path': None,
            'query': None,
            'fragment': None
        }

    def http_and_https(self, data):
        return self.url_pattern

    def ftp_and_ftps(self, data):
        return self.url_pattern

    def ssh(self, data):
        return self.url_pattern

    def git(self, data):
        return self.url_pattern

    def file(self, data):
        return self.url_pattern

    def rsync(self, data):
        return self.url_pattern

    def mailto(self, data):
        return self.url_pattern

    def telnet(self, data):
        return self.url_pattern

    def nntp(self, data):
        return self.url_pattern


from urllib.parse import urlparse
from urllib.parse import urlsplit


# url = 'https://user:pass@NetLoc.com:80/path;parxxam?query=argument#fragment'
# parsed = urlparse(url)
# print('scheme  :', parsed.scheme)
# print('netloc  :', parsed.netloc)
# print('path    :', parsed.path)
# print('params  :', parsed.params)
# print('query   :', parsed.query)
# print('fragment:', parsed.fragment)
# print('username:', parsed.username)
# print('password:', parsed.password)
# print('hostname:', parsed.hostname)
# print('port    :', parsed.port)
# print("---------------")
#
# parsed = urlsplit(url)
# print(parsed)
#

def parse_url(url: str):
    c = Parse()
    scheme_position = url.find(':')
    print(url, scheme_position)
    if scheme_position > 0:
        scheme_word = url[:scheme_position]
        if re.match(r'^(http|https)$', scheme_word):
            return c.http_and_https(url)
        elif re.match(r'^(ftp|ftps)$', scheme_word):
            return c.ftp_and_ftps(url)
        elif re.match(r'^(ssh)$', scheme_word):
            return c.ssh(url)
        elif re.match(r'^(git)$', scheme_word):
            return c.git(url)
        elif re.match(r'^(file)$', scheme_word):
            return c.file(url)
        elif re.match(r'^(rsync)$', scheme_word):
            return c.rsync(url)
        elif re.match(r'^(mailto)$', scheme_word):
            return c.mailto(url)
        elif re.match(r'^(telnet)$', scheme_word):
            return c.telnet(url)
        elif re.match(r'^(nntp)$', scheme_word):
            return c.nntp(url)
    return
