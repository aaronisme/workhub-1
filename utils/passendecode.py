"""
Statement:
    Encrypt and decrypt the password
Author:
    Will
Date:
    2014.11.10
"""

import base64
from Crypto.Cipher import AES
from Crypto import Random


KEY = 'YoU_c0u1d&n3ver%9U33s_hk'
def encrypt_string(content):
    iv = Random.new().read(AES.block_size)
    aes = AES.new(KEY, AES.MODE_CBC, iv)
    return base64.b64encode(iv + aes.encrypt(content))


def decrypt_string(content):
    pass


# Using base64 to encode and decode the key
def encode_key():
    enKey = base64.encodestring(KEY)
    return enKey

def decode_key(enKey):
    pass


if __name__ == "__main__":
    a = encrypt_string('adahekaihekaihekaihekai')
    print a