import os


def get_whois(url):
    print 'Retrieving whois information for ' + url
    command = 'whois ' + url
    try:
        process = os.popen(command)
        result = str(process.read())
        return result
    except Exception, e:
        print ('Unable to get whois information for ' + url + ' - ' + str(e))
