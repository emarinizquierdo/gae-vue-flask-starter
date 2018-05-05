import logging

from google.appengine.ext import ndb
from flask_restplus import abort

from src.beans.item import Item
import uuid

def create(args):

    if(not args.get('id', False)):
        args['id'] = str(uuid.uuid4())

    item = Item(
        **args
    )

    item.key = ndb.Key(Item, args['id'])
    
    item.put()

    return item

def update(id, args):

    get(id)
    args['id'] = id
    return create(args)


def get(id):

    item = ndb.Key(Item, id).get()
    if(item is None):
        abort(404, 'Item not found')

    return item

def list(offset, page_size):

    items = Item.query().order(Item.title).fetch(page_size, offset=offset)

    return items

def delete(id):

    item_key = ndb.Key(Item, id)
    item = item_key.get()

    if(item is None):
        abort(404, 'Item not found')

    item_key.delete()

    return None