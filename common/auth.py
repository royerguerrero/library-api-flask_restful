from flask import make_response, request

def auth_required(func):
    def wrapper(self):
        if request.authorization and request.authorization['username'] == 'royer' and request.authorization['password'] == '1234':
            return func(self)
        
        return make_response('Could not verify your login!', 401, {'WWW-Autencticate': 'Basic reaml="Login Required"'})

    return wrapper