# password-checker

Program to check if your password has been compromised

## Introduction

How do we know for sure? If password we use is known to some server or sitting elsewhere?
How many times has this question arisen in our minds?

Yes there are web sites that tell if password has been pwned.

Wouldn't it be nice if we could verify locally on a laptop? without submitting to websites?

Hence I came up with this utility to check if password is indeed compromised and tells a count too.

## Description

Modern application like netflix, fb, twitter, google all use "k anonymity", to know who you are and probably will never need to re-identify you but at the same time the data remains useful for their platform.

We will first encrypt the password to SHA1 submit first 5-chars and use "k anonymity".
If the API returns a list of records matching first 5-chars, we could then locally compare and count the rest of characters.

That ways, we never submit our password to any website/API and we do everything locally.

## Usage
    python3.8 checkpasssword.py <test_password_1> <test_password_2>

## Example
     python3.8 checkpasssword.py hello@123 india##12
