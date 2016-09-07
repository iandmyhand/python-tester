import base64

from Crypto.Hash import MD5
from Crypto.PublicKey import RSA
from Crypto import Random

plaintext = 'test'
random_generator = Random.new().read

# This will take a while...
RSAkey = RSA.generate(1024, random_generator)
hash = MD5.new(plaintext.encode('utf-8')).digest()
# print('type of hash:' + str(type(hash)))
signature = RSAkey.sign(hash, random_generator)
# print('type of signature:' + str(type(signature[0])))

# Print what an RSA sig looks like--you don't really care.
# print('signature:' + str(signature[0]))
# print('signature:' + str(len(str(signature[0]))))

# This sig will check out
# print('verify:' + str(RSAkey.verify(hash, signature)))

# This sig will check out
# print('verify:' + str(RSAkey.verify(hash[:-1], signature)))
# print('\n')

public_key = RSAkey.publickey()
public_key_pem = public_key.exportKey("PEM")
private_key_pem = RSAkey.exportKey("PEM")

# print(private_key_pem)
# print(public_key_pem)
# print(public_key_pem.decode('utf-8'))
# print('\n')

_encoded_bytes = base64.standard_b64encode(public_key_pem)
_decoded_str = _encoded_bytes.decode('utf-8')
# print(_decoded_str)
_decoded_bytes = base64.standard_b64decode(_encoded_bytes)
# print(str(_decoded_bytes))
_decoded_str2 = _decoded_bytes.decode('utf-8')
# print(_decoded_str2)
# print(_decoded_str == _decoded_str2)

_encoded_plain_text = base64.standard_b64encode(plaintext.encode('UTF-8'))
_encrypted_data = public_key.encrypt(_encoded_plain_text, len(_encoded_plain_text))
# print('encrypted_data: %s, %s' % (str(type(_encrypted_data)), str(_encrypted_data)))

_decrypted_data = RSAkey.decrypt(_encrypted_data)
_decrypted_plain_text = base64.standard_b64decode(_decrypted_data)
# print('decrypted_plain_text: ' + str(_decrypted_plain_text))


_encoded_text = 'UDKrSZPqWDNfNA201mWMFILp11BYJ3BqCxzp3RpB9Mvg3qlaZ2nmFAP6KNSmk/Uma8ENL/fvKXg+oHlgJuQwsmosyLTMOgw5YgcHVLaONT6XhNaqyGpVZ8Mx2bdM3Ij1yVF4A21v066LacR8ek55v9ncZFLz6XPrm5hzuYP0VLU='
_decoded_text = base64.standard_b64decode(_encoded_text.encode('UTF-8'))
print('decoded_text:' + str(_decoded_text))

_key = RSA.importKey('-----BEGIN RSA PRIVATE KEY-----\nMIICXQIBAAKBgQDY61+JoVEDDpGl6QBuFAfyoT7frmsxDQlxaQ6+SUBgHxxbd7du\nrUqaInjSuemVLBVDaKeFLdgQ52YF2PPOakmgp99Jmx4IW1DRG8tRhOP3VKObNrBZ\nOOzgbJ8i57QPB4lpVaIQqXGMwHnr6eBzlMDUJwN/HY9H/4wi9qgEE6HhAwIDAQAB\nAoGBALqgnzzpVqrboQHuWplakI/2nQKTrNOx1LsHWVDr8wAAJESp1l7Zp0K/f9ZF\nb6sRF2Y8p0xU6f15KPTE+NZR6e9CEoAxwKqird2Z8Oog7IXX8JOeXeMmWLNJtzvm\nTNZGS5mBJxl6DYGmHwn9rZnDWKzoF83MtsFfBevH1ooTBESxAkEA352qUGV79vpx\nzsyzTy/asVqvLG2K6eNPUP3dl/GIv+Hzlpg8kw/g+8GBSnvMPppd3kJLYSaqV9w/\nxwuowa/GmwJBAPhVcY/Ks/VWANQvrLm/imeNSBDiAZSP9qAPpSYF2nIftoXJv+Mn\nhEeDAmq6gdIrM20Rks5DRtez+qROc5pqQbkCQQCMWDwIcWk4PT8od7kiPfqXzT6c\nN7QzzwJ85pgpQOJ+66UiIzIBarndyDkJMmGh+OhpElqVAttugUFV/69OwK95AkBN\ni9jvbvvtI5MUr2J/inl8xph3dSvLKX15FAmdKvzA4HhNpOd/1oovDpEFpQH/EDB5\n4Z/3Ovj3SKN/BWSCFqY5AkBfVtXDZrUQW+AwYIZgJb0eD3vilCf7Q/QKUydyERCG\nOOYwtOx++57CJutd3JoKJPVRhmApj2P48pNvS53addkT\n-----END RSA PRIVATE KEY-----'.encode('UTF-8'))
_decrypted_text = _key.decrypt(_decoded_text)
print('decrypted_text:' + str(_decrypted_text))

from Crypto.Cipher import PKCS1_v1_5
_key_pkcs1 = PKCS1_v1_5.new(_key)
_error = dict()
_decrypted_text = _key_pkcs1.decrypt(_decoded_text, _error)
print('decrypted_text:' + str(_decrypted_text.decode('UTF-8')))
