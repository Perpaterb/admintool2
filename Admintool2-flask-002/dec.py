import base64 
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad,unpad

#AES ECB mode without IV

data = 'abcd1234567'
endata = '30BKf5b1zeDEkRBYuOfieA=='
key = '9f86d081884c7d65' #Must Be 16 char for AES128

def encrypt(raw):
        raw = pad(raw.encode(),16)
        cipher = AES.new(key.encode('utf-8'), AES.MODE_ECB)
        return base64.b64encode(cipher.encrypt(raw))

def decrypt(enc):
        enc = base64.b64decode(enc)
        cipher = AES.new(key.encode('utf-8'), AES.MODE_ECB)
        return unpad(cipher.decrypt(enc),16)

encrypted = encrypt(data)
print('encrypted ECB Base64:',encrypted.decode("utf-8", "ignore"))

decrypted = decrypt(endata)
print('data: ',decrypted.decode("utf-8", "ignore"))