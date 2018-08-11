import re
import json
from urllib.parse import urlparse


root_dir = 'example_data'
input_dir = '%s/input' % root_dir
output_dir = '%s/output/python' % root_dir


def extract_data(url: str):
    parsed = urlparse(url)
    return {
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


def parse_url(url: str):
    scheme_position = url.find(':')
    if scheme_position > 0:
        # 7. Application layer:
        # https://en.wikipedia.org/wiki/Application_layer
        # -----------------
        # Services:
        # BitTorrent • DNS • BOOTP
        # DHCP • FTP • HTTP • HTTPS • IMAP • IRC • Ident • NNTP • NFS • NTP • POP3
        # RTP • SIP • SMB • SMTP • SNMP • SSH • STUN • Telnet • XMPP
        scheme_word = url[:scheme_position]
        if re.match(r'^(http|https)$', scheme_word):
            return extract_data(url)
        elif re.match(r'^(ftp|ftps)$', scheme_word):
            pass
        elif re.match(r'^(ssh)$', scheme_word):
            pass
        elif re.match(r'^(git)$', scheme_word):
            pass
        elif re.match(r'^(file)$', scheme_word):
            pass
        elif re.match(r'^(rsync)$', scheme_word):
            pass
        elif re.match(r'^(mailto)$', scheme_word):
            pass
        elif re.match(r'^(telnet)$', scheme_word):
            pass
        elif re.match(r'^(nntp)$', scheme_word):
            pass
    return None


def save_to_file(fwp, parsed_data):
    json_data = json.dumps(parsed_data)
    with open(fwp, 'w') as f:
        f.write(json_data)


if __name__ == '__main__':
    for f in ['http.json', 'https.json']:
        fwp_input = '%s/%s' % (input_dir, f)
        fwp_output = '%s/%s' % (output_dir, f)

        data = {}
        with open(fwp_input) as f:
            for url in json.loads(f.read()):
                data[url] = {'data': parse_url(url)}

        save_to_file(fwp_output, data)
