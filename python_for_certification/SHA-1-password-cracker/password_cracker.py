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
20 行。use_salts=True の場合、パスワードの前、もしくは後ろにsalt 用の文字列を追加してからハッシュ化するとのこと。

https://docs.python.org/ja/3/library/hashlib.html

"""

def import_password():
    password_list = []
    with open('top-10000-passwords.txt', 'r') as f:
        password_list = f.read().split("\n")
    return password_list

def generate_password_hashed_dict(password_list, use_salts):
    hashed_dict = {}
    salts = import_salt()
    for password in password_list:
        if use_salts:
            for salt in salts:
                prepend_salted_password = salt + password;
                hashed_password = hashlib.sha1(prepend_salted_password.encode("utf-8")).hexdigest()
                hashed_dict[hashed_password] = password

                append_salted_password = password + salt;
                hashed_password = hashlib.sha1(append_salted_password.encode("utf-8")).hexdigest()
                hashed_dict[hashed_password] = password
        else:
            hashed_password = hashlib.sha1(password.encode("utf-8")).hexdigest()
            hashed_dict[hashed_password] = password
    return hashed_dict

def import_salt():
    salts = []
    with open('known-salts.txt', 'r') as f:
        salts = f.read().split("\n")
    return salts
