#!/usr/bin/env python

import json
import sys

def main():
    try:
        with open('cloudfront-distribution.json', 'r') as f:
            data = json.loads(f.read())
            with open('etag', 'w') as etag:
                etag.write(data['ETag'])
    except:
        sys.exit(1)

if __name__ == '__main__':
    main()
