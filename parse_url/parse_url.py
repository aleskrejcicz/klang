import os
import json
from urllib.parse import urlparse


root_dir = 'example_data'
input_dir = '%s/input' % root_dir
output_dir = '%s/output/python' % root_dir


def ext_data(fwp):
    parsed_data = {}
    with open(fwp) as f:
        for url_data in json.loads(f.read()):
            url = url_data['url']
            parsed = urlparse(url)
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
                'port': parsed.port
            }
    return parsed_data


def save_to_file(fwp, parsed_data):
    json_data = json.dumps(parsed_data)
    with open(fwp, 'w') as f:
        f.write(json_data)


for f in ['http.json', 'https.json']:
    fwp_input = '%s/%s' % (input_dir, f)
    fwp_output = '%s/%s' % (output_dir, f)
    save_to_file(fwp_output, ext_data(fwp_input))
