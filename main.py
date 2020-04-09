from flask import Flask, jsonify
from flask_restful import Api
from resources.books import Book, BookList

app = Flask(__name__)
api = Api(app)

api.add_resource(BookList, '/books')
api.add_resource(Book, '/books/<book_id>')

if __name__ == '__main__':
    app.run(debug=True)
