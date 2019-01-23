#!/usr/bin/env python

import json
import sys

def main():
    if not sys.argv[1]:
        sys.exit(2)
    try:
        with open('update-distribution.json', 'w') as f:
            config = read_config()
            config['Origins']['Items'][0]['OriginPath'] = '/' + sys.argv[1]
            f.write(json.dumps(config))
    except:
        sys.exit(1)

def read_config():
    with open('cloudfront-distribution.json', 'r+') as f:
            data = json.loads(f.read())
            return data['DistributionConfig']

if __name__ == '__main__':
    main()
