from hashlib import sha256
txt = "jamin"
cod = txt.encode('utf-8')
hash = sha256(cod).hexdigest()

print(hash)