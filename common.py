import json
import argparse
def readconfig(path):
    filestr = ''
    with open(path, 'r') as f:
        filestr = f.read()
    if filestr[len(filestr) - 1] != '\n':
        filestr = filestr + '\n'
    return filestr
def writeconfig(path, filestr):
    with open(path, 'w') as f:
        f.write(filestr)
        f.close()


def parsearguments():
    parser = argparse.ArgumentParser()
    parser.add_argument('--proxyon', action='store_true', default=False,
                    dest='proxyon',
                    help='Turn proxy on')
    parser.add_argument('--proxyoff', action='store_true', default=False,
                dest='proxyoff',
                help='Turn proxy off')
    parser.add_argument('--username', action='append', required=False,
                const=None,
                help='Username')
    parser.add_argument('--password', action='append', required=False,
                const=None,
                help='Password')
    parser.add_argument('--host', action='append', required=False,
                const=None,
                help='Host')
    parser.add_argument('--port', action='append', required=False,
                const=None,
                help='Port')
    results = parser.parse_args()

    return results