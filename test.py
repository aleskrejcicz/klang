from urllib.parse import urlparse
from urllib.parse import urlsplit


url = 'https://user:pass@NetLoc.com:80/path;parxxam?query=argument#fragment'
parsed = urlparse(url)
print('scheme  :', parsed.scheme)
print('netloc  :', parsed.netloc)
print('path    :', parsed.path)
print('params  :', parsed.params)
print('query   :', parsed.query)
print('fragment:', parsed.fragment)
print('username:', parsed.username)
print('password:', parsed.password)
print('hostname:', parsed.hostname)
print('port    :', parsed.port)
print("---------------")

parsed = urlsplit(url)
print(parsed)

