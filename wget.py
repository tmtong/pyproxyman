import re
import argparse
import common
def proxyoff(filestr):
    filestr = re.sub(r'\w*use_proxy.*\n', '', filestr)
    filestr = re.sub(r'\w*http_proxy.*\n', '', filestr)
    filestr = re.sub(r'\w*https_proxy.*\n', '', filestr)
    return filestr
def proxyon(filestr,  host, port, username = None, password = None):
    filestr = proxyoff(filestr)
    filestr = filestr  + 'use_proxy = on\n'
    if username == None:
        filestr = filestr + 'http_proxy=' + host + ':' + str(port) + '\n'
        filestr = filestr + 'https_proxy=' + host + ':' + str(port) + '\n'

    else:
        filestr = filestr +  'http_proxy=' + username + ':' + password + '@' + host + ':' + str(port) + '\n'
        filestr = filestr +  'https_proxy=' + username + ':' + password + '@' + host + ':' + str(port) + '\n'
    return filestr
def test(filestr,  host, port, username = None, password = None):
    print(filestr)
    print(host)
    print(port)
    print(username)
    print(password)

if __name__ == '__main__':


    results = common.parsearguments()
    path = './wgetrc'
    filestr = common.readconfig(path)
    # filestr = proxyoff(filestr)
    # filestr = proxyon(filestr, 'proxy.home', 8080,  'username', 'password')
    # common.writeconfig(path, filestr)
    if results.proxyon:
        filestr = proxyon(filestr, results.host[0], results.port[0],  results.username[0], results.password[0])
        common.writeconfig(path, filestr)
    if results.proxyoff:
        proxyoff(filestr)
        common.writeconfig(path, filestr)