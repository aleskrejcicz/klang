import json
from urllib.parse import urlparse


root_dir = 'example_data'
filename = 'url.http.json'


def extract(root_dir, filename):
    parsed_data = {}
    with open('%s/input/%s' % (root_dir, filename)) as f:
        for url in json.loads(f.read()):
            parsed = urlparse(url)
            try:
                port = parsed.port
            except Exception as e:
                port = None

            parsed_data[url] = {
                'scheme': parsed.scheme,
                'netloc': parsed.netloc,
                'path': parsed.path,
                'params': parsed.params,
                'query': parsed.query,
                'fragment': parsed.fragment,
                'username': parsed.username,
                'password': parsed.password,
                'hostname': parsed.hostname,
                'port': port
            }
    return parsed_data


def save(root_dir, filename, parsed_data):
    with open('%s/output/python/%s' % (root_dir, filename), 'w') as f:
        f.write(json.dumps(parsed_data))


parsed_data = extract(root_dir, filename)
save(root_dir, filename, parsed_data)
