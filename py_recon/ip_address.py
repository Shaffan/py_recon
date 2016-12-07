import os
import platform


def get_ip_address(url):
    print 'Getting ip address for ' + url
    if platform.system() == 'Windows':
        command = "nslookup " + url

        process = os.popen(command)
        results = list(process)
        marker = ''
        ip = ''
        print results
        for item in results:
            if 'Address' in item:
                marker = item.find('Address: ') + 10
                ip = item[marker:].splitlines()[0]
        return ip
    else:
        command = "host " + url

        print('No unix-based implementation')