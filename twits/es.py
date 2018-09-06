import os

from elasticsearch import Elasticsearch


class ESClient(object):
    ES_HOST = os.environ.get('ES_HOST', 'localhost')
    ES_PORT = int(os.environ.get('ES_HOST', '9200'))
    ES_INDEX = os.environ.get('ES_INDEX', 'twits')

    es = Elasticsearch()

    def insert_entry(self, data):
        self.es.index(index=self.ES_INDEX, doc_type='twit', body=data)
