import requests
import hashlib
import sys


# has the input
# pull the 1st 5 chars
# rest of the chars as tail
# send the first 5 chars to API, get response

def hash_the_given_password(pwd):
    return hashlib.sha1(pwd.encode('UTF-8')).hexdigest().upper()


def get_api_response(first_5_hash_chars):
    response = requests.get(f'https://api.pwnedpasswords.com/range/{first_5_hash_chars}')

    if response.status_code != 200:
        raise RuntimeError(f'Invalid request, kindly check your password {first_5_hash_chars}')
    else:
        return response


def check_if_used(pwd):
    hashed_pwd = hash_the_given_password(pwd)
    first_5_hash_chars, tail = hashed_pwd[:5], hashed_pwd[5:]

    response = get_api_response(first_5_hash_chars)
    hashes = (line.split(':') for line in response.text.splitlines())

    for h, count in hashes:
        if tail == h:
            return count
    return 0


def main(args):
    for pwd in args:
        count = check_if_used(pwd)
        if count:
            print(f'"{pwd}" discovered {count} times, you may NOT want to use this anywhere!!')
        else:
            print(f'{count} instances found, carry on! ')

    print('Done!')


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
