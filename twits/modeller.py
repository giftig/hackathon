import datetime


class Modeller(object):
    """
    Remodels JSON into a consistent format
    """
    # TODO: Get data for this
    EMOTION_WORDS = ['cool', 'sentiment']

    def _find_emotions(self, text):
        return [w for w in self.EMOTION_WORDS if w in text.lower()]

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

        return {
            'keywords': hashtags,
            'emotions': self._find_emotions(text),
            'raw_text': text,
            'timestamp': self._format_time(created)
        }
