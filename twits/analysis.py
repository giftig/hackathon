import requests


class Analyser(object):
    """
    Arbitrarily analyse some text and produce some weightings
    """
    API_URL = 'http://text-processing.com/api/sentiment/'

    def analyse(self, text):
        res = requests.post(
            self.API_URL,
            {'text': text}
        ).json()
        probs = res['probability']

        best_value = 0
        best_key = None

        for k, v in probs.iteritems():
            if v > best_value:
                best_key = k
                best_value = v

        probs['decision'] = best_key

        return probs
