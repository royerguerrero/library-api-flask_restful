from flask import Flask, request, make_response, jsonify
from flask_restful import Api
from resources.books import Book, BookList
from config import Config
import jwt, datetime

app = Flask(__name__)
app.config.from_object(Config)

api = Api(app)

api.add_resource(BookList, '/books')
api.add_resource(Book, '/books/<book_id>')

@app.route('/login')
def login():
    auth = request.authorization

    if auth and auth.password == '1234':
        token = jwt.encode({'user': auth.username, 'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=30)}, app.config['SECRET_KEY'])
        return jsonify({'token': token.decode('UTF-8')})

    return make_response('Could not verify!', 401, {'WWW-Authenticate': 'Basic realm="Login Requiered"'})

if __name__ == '__main__':
    app.run(debug=True)