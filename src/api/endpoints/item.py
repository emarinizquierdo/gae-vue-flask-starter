# encoding: utf-8
# pylint: disable=too-few-public-methods,invalid-name,bad-continuation
"""
RESTful API User resources
--------------------------
"""

import logging

from flask_restplus import Resource, abort
from google.appengine.ext import ndb
import src.beans.mocks as mocks
import src.biz.item as ItemBiz

from src.restplus import api

log = logging.getLogger(__name__)

ns = api.namespace('items', description='Operations related to item entities')

parser = ns.parser()

@ns.route('',methods=['GET','POST'])
class Items(Resource):

    parser.add_argument('offset', type=int)
    parser.add_argument('page_size', type=int)
    @api.doc(description = 'List items with pagination', parser=parser)
    @ns.marshal_list_with(mocks.schema)
    def get(self):
        args = parser.parse_args()
        return ItemBiz.list(args['offset'], args['page_size'])

    @api.doc(description = 'Create a new item')
    @ns.expect(mocks.inputItem_schema)
    @ns.marshal_with(mocks.schema)
    def post(self):
        log.info("Creating item: ", api.payload)
        return ItemBiz.create(api.payload)

        
@ns.route('/<string:id>', methods=['GET','PUT','DELETE'])
class Items_id(Resource):

    @api.doc(description = 'Get an item by id')
    @ns.marshal_with(mocks.schema)
    def get(self,id):
        return ItemBiz.get(id)

    @api.doc(description = 'Update an item by id')
    @ns.expect(mocks.inputItem_schema)
    @ns.marshal_with(mocks.schema)
    def put(self, id):
        return ItemBiz.update(id, api.payload)

    @api.doc(description = 'Delete an item by id')
    def delete(self, id):
        return ItemBiz.delete(id)