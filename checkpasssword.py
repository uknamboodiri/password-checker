import requests
import hashlib

pwd = 'hello'

SHA1_Hash = hashlib.sha1(pwd.encode('UTF-8')).hexdigest().upper()
first_5_hash_chars, tail = SHA1_Hash[:5], SHA1_Hash[5:]

response = requests.get(f'https://api.pwnedpasswords.com/range/{first_5_hash_chars}')
hashes = (line.split(':') for line in response.text.splitlines())

for h, count in hashes:
    # print(h, count)
    if tail == h:
        print(count)
        break
