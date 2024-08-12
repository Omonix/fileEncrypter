import random
import string

todo = input('\033[1;34mDo you want encrypt or decrypt file ? e/d ')
chars = string.printable

def genPassword(length):
    pwd = ""
    i = 0
    while i < int(length):
        pwd = pwd + random.choice(chars)
        i = i + 1
    return pwd
def vigenere(message, key, direction=1):
    key_index = 0
    encrypted_message = ''
    for letter in message:
        key_char = key[key_index % len(key)]
        key_index += 1
        offset = chars.index(key_char)
        index = chars.find(letter)
        new_index = (index + offset*direction) % len(chars)
        encrypted_message += chars[new_index]
    return encrypted_message
def decrypt(message, key):
    return vigenere(message, key, -1)
def encrypt(message, key):
    return vigenere(message, key)

if todo == 'e':
    data = input("\033[1;33mFile to encrypt : \033")
    file = open(data, 'r')
    hasher = genPassword(input('\033[1;36mLength security : '))
    encrypted = encrypt(file.read(), hasher)
    print(f"\033[1;92m\nKey : \033[1;35m{hasher}\n\033[1;92mEncrypted data: \033[1;35m{encrypted}\033[0m")
    file= open(data, 'w')
    file.write(encrypted)
    file.close()
elif todo == 'd':
    data = input('\033[1;33mFile to decrypt : ')
    file = open(data, 'r')
    hasher = input('\033[1;36mKey : ')
    encrypted = decrypt(file.read(), hasher)
    print(f'\033[1;92m\nDecrypted data : \033[1;35m{encrypted}')
    registre = input('\033[1;34mSave data ? y/n ')
    if registre == 'y':
        file= open(data, 'w')
        file.write(encrypted)
        print('\033[1;92mRegistred\033[0m')
    else:
        print('\033[1;31mNot Registred\033[0m')
    file.close()
else:
    print(f'\033[1;31mError : \'{todo}\'\033[0m')