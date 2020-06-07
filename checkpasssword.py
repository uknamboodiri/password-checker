import requests
import sys
import hashlib


def get_api_response(first_5_chars):
    response = requests.get(f'https://api.pwnedpasswords.com/range/{first_5_chars}')

    if response.status_code != 200:
        raise RuntimeError('Please check, something went wrong')

    return response


def get_leak_count(pwd):
    sha1_hashed_pwd = hashlib.sha1(pwd.encode('UTF-8')).hexdigest().upper()
    first_5_chars, other_chars = sha1_hashed_pwd[:5], sha1_hashed_pwd[5:]

    matched_hash_strings_list = get_api_response(first_5_chars)

    hashed_list = (line.split(':') for line in matched_hash_strings_list.text.splitlines())
    for h, count in hashed_list:
        if h == other_chars:
            return count

    return 0


def main(pwds):
    for pwd in pwds:
        count = get_leak_count(pwd)
        if count:
            print(f'"{pwd}" discovered {count} times, you may NOT want to use anymore!')
        else:
            print(f'"{pwd}" discovered {count} times, all good safe to use!')

    print('Done!')


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
