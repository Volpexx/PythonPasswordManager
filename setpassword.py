import base64
import os, sys



with open('login.txt', 'w', encoding='utf-8') as mPassword:
    unincoded_pass = input("Set Master Password: ")
    encoded_pass = unincoded_pass.encode('cp037')
    mPassword.write(str(encoded_pass))
    print(encoded_pass)
    mPassword.close()

   