import base64
import hashlib

from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_v1_5


def encode_with_rsa_pub():
    _public_key_uuid = '1621d08f-859f-448f-ae01-bdef538afa36'
    _salt_uuid = 'ab68610f-8969-4e36-83a6-feaff3d1bbd1'
    _salt = 'f1776ef6-6a5d-4499-9183-3f5eb672cd43'
    _rsa_public_pem_key = 'LS0tLS1CRUdJTiBQVUJMSUMgS0VZLS0tLS0KTUlHZk1BMEdDU3FHU0liM0RRRUJBUVVBQTRHTkFEQ0JpUUtCZ1FDaEZKYUg3dWlCeUN5WUNVbjg1NnJVY2RuMQo2UElQaW1SNDZPS1N1NkVDK1cxb2V2a0didVJSN1FiRTlHU3Q2dXEzR3ZLWlNNOWJubEQzQ2UzU1duUjNkb3EwClZjK0x4cUFpWXFGM1M2NHR4elhyNmFRWG5IbndubnZyY29pTkE5Rzl0d1VZVmlwaGp2ZUc2SXhYanloZUxwVUMKN1Q0Yk1haFJ0Y1VmUFFpQ1B3SURBUUFCCi0tLS0tRU5EIFBVQkxJQyBLRVktLS0tLQ=='


    """
    Encode with RSA Public PEM Key string
    """
    _decoded_public_key = base64.standard_b64decode(_rsa_public_pem_key.encode('utf-8'))
    _rsa_public_key_pkcs1 = PKCS1_v1_5.new(RSA.importKey(_decoded_public_key))
    _encrypted_data = list()
    _encrypted_data.append(_public_key_uuid)
    _encrypted_data.append(_salt_uuid)
    for i in range(6):
        _encrypted_plain = _rsa_public_key_pkcs1.encrypt((str(i+1) + _salt).encode('utf-8'))
        _encrypted_string = base64.standard_b64encode(_encrypted_plain).decode('utf-8')
        _encrypted_data.append(_encrypted_string)
    print(','.join(_encrypted_data))


def hash_by_sha256():
    sha_signature = hashlib.sha256('test'.encode()).hexdigest()
    print(sha_signature.upper())


if __name__ == '__main__':
    hash_by_sha256()
