# example execution
# terminal: 
# python password_checker/password_checker.py hello dragon0072 knowledgezone123
# hello was found 403640 times, you shall change the password
# dragon0072 was found 161 times, you shall change the password
# knowledgezone123 was not found. Please continue using it.

import requests
import hashlib
import sys

def request_api_data(query_char):
    url = "https://api.pwnedpasswords.com/range/" + query_char
    res = requests.get(url)
    # print(res)

    if res.status_code != 200:
        raise RuntimeError(f"Response: {res.status_code}, Error fetching data! check api and try again!")
    return res

def get_password_leaks_count(hashes, hash_to_check):
    for line in hashes.text.splitlines():
        hash, count = line.split(":")

        if hash == hash_to_check:
            return count
    return 0

def pwned_api_check(password):
    sha1pass = hashlib.sha1(password.encode('utf-8')).hexdigest().upper()
    prefix, suffix = sha1pass[:5], sha1pass[5:]
    
    response = request_api_data(prefix)
    
    return get_password_leaks_count(response, suffix)

def main(args):
    # print(args)
    for password in args:
        count = pwned_api_check(password)

        if count:
            print(f"{password} was found {count} times, you shall change the password")
        else:
            print(f"{password} was not found. Please continue using it.")

    return 'done'

if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))