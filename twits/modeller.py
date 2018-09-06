import datetime
import requests

import analysis


class Modeller(object):
    """
    Remodels JSON into a consistent format
    """
    def __init__(self, analyser=analysis.Analyser()):
        self.analyser = analyser

    @staticmethod
    def _format_time(dt):
        return dt.isoformat()

    def model_tweet(self, tweet):
        hashtags = [
            h['text'] for h in tweet.get('entities', {}).get('hashtags', [])
        ]
        text = tweet['text']
        ts = int(tweet['timestamp_ms'])

        created = datetime.datetime.utcfromtimestamp(ts // 1000)
        author_weighting = tweet.get('user', {}).get('followers_count', 0)

        data = {
            'author_weighting': author_weighting,
            'keywords': hashtags,
            'raw_text': text,
            'source': 'twitter',
            'timestamp': self._format_time(created)
        }
        # Flattened for easier modelling
        data.update({
            'emotion_analysis.%s' % k: v
            for k, v in self.analyser.analyse(text).iteritems()
        })
        return data
