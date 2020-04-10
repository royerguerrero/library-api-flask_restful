from flask import Flask, jsonify
from flask_restful import Api
from resources.books import Book, BookList
from common.auth import generate_hash

app = Flask(__name__)
api = Api(app)

api.add_resource(BookList, '/books')
api.add_resource(Book, '/books/<book_id>')
hash_api = generate_hash()
print(hash_api)

if __name__ == '__main__':
    app.run(debug=True)