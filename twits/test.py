#!/usr/bin/env python2.7

import json
import os

from modeller import Modeller

def main():
    data = []

    for f in os.listdir('data/tweets'):
        if not f.endswith('.json'):
            continue

        f = os.path.join('data/tweets', f)
        with open(f) as fp:
            data.append(json.load(fp))

    m = Modeller()
    data = [m.model_tweet(e) for e in data]

    print json.dumps(data)

if __name__ == '__main__':
    main()
