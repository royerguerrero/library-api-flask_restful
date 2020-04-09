from flask import jsonify, make_response
from flask_restful import Resource, abort, reqparse
from common.db import BOOKS
import ast

parser = reqparse.RequestParser()
parser.add_argument('book_data')

def abort_if_book_doesnt_exits(book_id):
    if book_id not in BOOKS:
        abort(404, message='El libro con id {} no existe'.format(book_id))

class BookList(Resource):
    def get(self):
        return jsonify({'data': BOOKS})
    def post(self):
        args = parser.parse_args()
        BOOKS[str(len(BOOKS) + 1)] = ast.literal_eval(args['book_data'])
        print(BOOKS)
        return make_response(jsonify({'message':'successful creation'}), 201)
        

class Book(Resource):
    def get(self, book_id):
        abort_if_book_doesnt_exits(book_id)
        return jsonify({'data': BOOKS[book_id]})

    def put(self, book_id):
        abort_if_book_doesnt_exits(book_id)
        args = parser.parse_args()
        BOOKS[book_id] = ast.literal_eval(args['book_data'])
        print(BOOKS)
        return jsonify({'message':'successful modification'})

    def delete(self, book_id):
        abort_if_book_doesnt_exits(book_id)
        args = parser.parse_args()
        del BOOKS[book_id]
        print(BOOKS)
        return jsonify({'message':'successful delete'})
        
