import hmac, hashlib
key_hash = hmac.new(key=b'secret', digestmod=hashlib.sha1)
key_hash.update(b'time')
key_hash.update(b'uid')

print(key_hash.hexdigest())

client_hash = hashlib.sha1(b'uid')
client_hash.update(b'time')
client_hash.update(b'secret')
print(client_hash.hexdigest())

print(hmac.compare_digest(key_hash.digest(), client_hash.digest()))
