"""
https://pypi.org/project/bcrypt/

pip install bcrypt

明碼保存進 db 很危險, 這邊使用 bcrypt 加密(hash)後再保存進去 db
(Hash Value 不可逆)


和 hashlib 相比, bcrypt 是專門為了安全儲存密碼加密用的.
"""

import bcrypt

def ex1():
    print('加密 user password')
    user_input_pwd = 'mypassword'
    passwd = user_input_pwd.encode('utf-8')
    salt = bcrypt.gensalt(rounds=16) # rounds 越大越安全, 但加密時間越久
    hashed_pwd = bcrypt.hashpw(passwd, salt)
    print('hashed_pwd:', hashed_pwd)
    save_db_pwd = hashed_pwd.decode('utf-8')
    print('save db:', save_db_pwd)

    print('開始驗證')
    print('user input pwd:', user_input_pwd)
    if bcrypt.checkpw(user_input_pwd.encode('utf-8'), save_db_pwd.encode('utf-8')):
        print("match")
    else:
        print("does not match")


if __name__ == "__main__":
    ex1()