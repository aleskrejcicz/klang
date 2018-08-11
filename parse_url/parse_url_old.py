import json
import re


class Parse:
    def http_and_https(self, data):
        return None

    def ftp_and_ftps(self, data):
        return None

    def ssh(self, data):
        return None

    def git(self, data):
        return None

    def file(self, data):
        return None

    def rsync(self, data):
        return None

    def mailto(self, data):
        return None

    def telnet(self, data):
        return None

    def nntp(self, data):
        return None


def parse_url(url: str):
    c = Parse()
    scheme_position = url.find(':')
    print(url, scheme_position)
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
