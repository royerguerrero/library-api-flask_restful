from flask import make_response, request
import hmac, hashlib, time

SECRET = 'TOP SECRET! SHHH'

def generate_hash():
    timestamp = str(int(time.time()))

    hash_api = hmac.new(key=SECRET.encode(), digestmod=hashlib.sha1)
    hash_api.update('1'.encode()) #UID
    hash_api.update(timestamp.encode()) # TIMESTAMP (Seg)
    data = {'hash': hash_api.hexdigest(), 'timestamp': timestamp}
    return data

def auth_required(func):
    def wrapper(self):
        hash_api = request.headers.get('X-HASH')
        hash_client = hmac.new(key=SECRET.encode(), digestmod=hashlib.sha1)
        hash_client.update(request.headers.get('X-UID').encode()) #UID
        hash_client.update(request.headers.get('X-TIMESTAMP').encode()) # TIMESTAMP (Seg)
        
        if hash_api == hash_client.hexdigest():
            return func(self)

        return make_response('Could not verify your login!', 401, {'WWW-Autencticate': 'Basic reaml="Login Required"'})

    return wrapper