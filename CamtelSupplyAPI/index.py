from algoliasearch_django import AlgoliaIndex
from algoliasearch_django.decorators import register
from .models import Product, Supplier

@register(Product)
class ProductIndex(AlgoliaIndex):
    fields = [
        'name',
        'category'
    ]
    """ settings = {
        'searchableAttributes' : ['title', 'content'],
    } """


@register(Supplier)
class SupplierIndex(AlgoliaIndex):
    fields = [
        'name',
        'number'
    ]