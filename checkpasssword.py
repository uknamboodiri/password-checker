"""Program to check if your password has been compromised

Introduction:
    How do we know for sure? if password we use everyday is already known to some server or sitting elsewhere?
    How many times has this question arisen in our minds?

    Yes there are web sites that tell if password has been pwned. Then again can we trust these websites?
    How do we trust these sites? Will they not use it? to their advantage?

    Wouldn't it be cool if we have have the ability to verify locally on the laptop? without submitting to websites?

    Hence I came up with this utility program that will check if your password is indeed compromised and tells
    a count too.

Description:
    Modern application like netflix, fb, twitter, google all use "k anonymity",
    to know who you are and probably will never need to re-identify you but at the same time the data remains useful for their platform.

    We will first encrypt the password to SHA1 submit first 5-chars and use "k anonymity".
    If the API returns a list of records matching first 5-chars, we could then locally compare and count the rest of characters.

    That ways, we never submit our password to any website/API and we do everything locally.

Usage:
    python3.8 checkpasssword.py <test_password_1> <test_password_2>

Example:
     python3.8 checkpasssword.py hello@123 india##12
"""

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
