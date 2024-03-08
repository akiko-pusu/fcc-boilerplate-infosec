import hashlib

def crack_sha1_hash(hash, use_salts = False):
    password_list = import_password()
    hased_list = generate_password_hashed_dict(password_list, use_salts)

    try:
        retval = hased_list[hash]
        print(retval)
        return retval
    except KeyError:
        return "PASSWORD NOT IN DATABASE"

"""
Create a function that takes in a SHA-1 hash of a password and returns the password
if it is one of the top 10,000 passwords used.
hash 化されたパスワードを引数とします。
復号されたパスワードがよくあるパスワードトップ10000のリストに存在しなければ、その値を返します。

(1) top-10000-passwords.txt
10000行あります。
ここから sha-1 の辞書を作って、いわゆる辞書攻撃的に総当たりすれば良さそう。

(2) known-salts.txt
20 行。

https://docs.python.org/ja/3/library/hashlib.html

"""

def import_password():
    password_list = []
    with open('top-10000-passwords.txt', 'r') as f:
        password_list = f.read().split("\n")
    print(len(password_list))
    return password_list

def generate_password_hashed_dict(password_list, use_salts = False):
    hased_dict = {}
    for password in password_list:
        hased_password = hashlib.sha1(password.encode("utf-8")).hexdigest()
        hased_dict[hased_password] = password
    return hased_dict
