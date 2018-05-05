from flask_restplus import fields
from src.restplus import api

inputItem_schema = api.model('inputItem', {
    'title': fields.String,
    'description': fields.String
})

schema = api.model('Item', {
    'id': fields.String,
    'title': fields.String,
    'description': fields.String
})