from algoliasearch_django import algolia_engine

def get_client():
    return algolia_engine.client

def get_index(index_name):
    client = get_client()
    index = client.init_index(index_name)
    return index

def perform_search(query, index_name, **kwargs):
    index = get_index(index_name)
    results = index.search(query)
    return results
