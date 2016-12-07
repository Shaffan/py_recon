from urllib2 import Request, urlopen
import io


def get_robots_txt(url):
    print 'Getting robots.txt for ' + url
    if url.endswith('/'):
        path = url
    else:
        path = url + '/'
    try:
        req = Request(path + 'robots.txt', data=None)
        response = urlopen(req)
        return response.read()
    except Exception, e:
        print ('Unable to get robots.txt - ' + str(e))
        return ''
