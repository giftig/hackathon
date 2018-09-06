import datetime

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

    @staticmethod
    def _contains_terms(text, terms):
        text = text.lower()
        terms = [t.lower() for t in terms]

        for t in terms:
            if t in text:
                return True

        return False

    def model_tweet(self, tweet, search_terms=None):
        text = tweet['text']

        if search_terms and not self._contains_terms(text, search_terms):
            return None

        hashtags = [
            h['text'] for h in tweet.get('entities', {}).get('hashtags', [])
        ]
        ts = int(tweet['timestamp_ms'])

        created = datetime.datetime.utcfromtimestamp(ts // 1000)
        author_weighting = tweet.get('user', {}).get('followers_count', 0)

        data = {
            'author_weighting': author_weighting,
            'keywords': hashtags,
            'raw_text': text,
            'search_terms': search_terms or [],
            'source': 'twitter',
            'timestamp': self._format_time(created)
        }
        # Flattened for easier modelling
        data.update({
            'emotion_analysis.%s' % k: v
            for k, v in self.analyser.analyse(text).iteritems()
        })
        return data
