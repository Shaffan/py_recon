from tld import get_tld


def get_domain_name(url):
    print 'Retrieving top level domain name for ' + url
    domain_name = get_tld(url)
    return domain_name
