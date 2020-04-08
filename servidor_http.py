from flask import Flask, jsonify
from flask_restful import Resource, Api, abort

app = Flask(__name__)
api = Api(app)

BOOKS = {
    '1': {
        'isbn': '744586',
        'title': 'Cien años de soledad',
        'description': 'Lorem insup lol.',
        'autor': 'Gabriel Garcia Marquez'
    },
    '2': {
        'isbn': '7894546',
        'title': 'De animales a dioses',
        'description': 'Lorem insup lol.',
        'autor': 'Yuval Noah Harari'
    }
}


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

    
class Authors(Resource):
    pass

class Generes(Resource):
    pass

api.add_resource(BookList, '/books')
api.add_resource(Book, '/books/<book_id>')
api.add_resource(Authors, '/authors')
api.add_resource(Generes, '/generes')

if __name__ == '__main__':
    app.run(debug=True)
