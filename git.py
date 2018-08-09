"""
http - mozna -> hledat bitbucket
https - mozna -> hledat bitbucket
ssh - mozna -> hledat ...

*.git 100%
ssh://git@* 100%
git@* 100%

bitbucket.org 90%
github.com 90%
gitlab.com 90%
"""

import json


with open('../php/php_urls.json') as data_file:
    urls = json.load(data_file)
    for url in urls.keys():
        if url.startswith(('ssh://git@', 'git@')) or url.endswith('.git'):
            print(url)
