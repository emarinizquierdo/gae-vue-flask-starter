from google.appengine.ext import ndb

class Item(ndb.Model):
    id = ndb.StringProperty()
    title = ndb.StringProperty()
    description = ndb.StringProperty()