from flask import Blueprint, jsonify
from flask_restful import Resource, abort
from common.db import BOOKS

def abort_if_book_doesnt_exits(book_id):
    if book_id not in BOOKS:
        abort(404, message='El libro con id {} no existe'.format(book_id))

class BookList(Resource):
    def get(self):
        return jsonify({'data': BOOKS})
    def post(self):
        pass

class Book(Resource):
    def get(self, book_id):
        abort_if_book_doesnt_exits(book_id)
        return jsonify({'data': BOOKS[book_id]})