import os

from elasticsearch import Elasticsearch


class ESClient(object):
    ES_PROTO = os.environ.get('ES_PROTO', 'https')
    ES_HOST = os.environ.get('ES_HOST', 'localhost')
    ES_PORT = int(os.environ.get('ES_PORT', '9200'))
    ES_INDEX = os.environ.get('ES_INDEX', 'twits')

    es = Elasticsearch('%s://%s:%s' % (ES_PROTO, ES_HOST, ES_PORT))

    def insert_entry(self, data):
        self.es.index(index=self.ES_INDEX, doc_type='twit', body=data)
