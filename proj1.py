from Crypto.Cipher import AES, ARC4, DES3
import base64
import codecs
import sys
import os.path
import os
import binascii
from colorama import init
from termcolor import cprint
from pyfiglet import figlet_format

init(strip=not sys.stdout.isatty())  # strip colors if stdout is redirected             # the big banner R O C K Y
cprint(figlet_format('R O C K Y', font='larry3d'), color='yellow', attrs=['bold'])


def banner(text, ch='-', length=39):                                                    # the small banner --- ---
    spaced_text = ' %s ' % text
    banner = spaced_text.center(length, ch)
    print(banner)


text = 'ROCKY CRYPTO TOOL'
banner(text)

print("\n")


def ceaser_enc(message, key):
    a = []
    cipher = ''
    char = 'a'
    while char <= 'z':
        a.append(char)
        char = chr(ord(char) + 1)
    for ch in message:
        if ch.isalpha():
            for i in range(26):
                if ch == a[i]:
                    x = i + key
                    if x > 25:
                        x = x % 26
                        cipher += a[x]
                    else:
                        cipher += a[x]
        else:
            cipher += ' '
    print("\n #|>#|># your Encrypted message: ", cipher, "\n")


def ceaser_dec(message, key):
    a = []
    text = ''
    char = 'a'
    while char <= 'z':
        a.append(char)
        char = chr(ord(char) + 1)
    for ch in message:
        if ch.isalpha():
            for i in range(26):
                if ch == a[i]:
                    x = i - key
                    if x < 0:
                        x = x % 26
                        text += a[x]
                    else:
                        text += a[x]
        else:
            text += ' '
    print("\n #<|#<|# your Decrypted message: ", text, "\n")


def AES_enc_messege(message, key, iv):
    if len(message) % 16 != 0:
        message += b' ' * (16 - (len(message) % 16))

    new = AES.new(key, AES.MODE_CBC, iv)
    enc = new.encrypt(message)
    encoding = base64.b64encode(enc)
    print("\n #|>#|># your Encrypted message: ", codecs.decode(encoding, 'utf-8'), "\n")


def AES_dec_message(message, key, iv):
    dec = base64.b64decode(message)
    new = AES.new(key, AES.MODE_CBC, iv)
    dy = new.decrypt(dec)
    encoding = codecs.decode(dy, 'utf-8')
    print("\n #<|#<|# your Decrypted message: ", encoding, "\n")


def AES_enc_files(file_name, key, iv):
    file_size = str(os.path.getsize(file_name)).zfill(16).encode('ascii')
    new_file = input("write the complete path where you want to save the file with the extension: ")
    read_size = 1024
    new = AES.new(key, AES.MODE_CBC, iv)
    with open(file_name, 'rb') as f1:
        with open(new_file, 'wb') as f2:
            f2.write(file_size)
            while True:
                data = f1.read(read_size)
                if len(data) == 0:
                    break
                elif len(data) % 16 != 0:
                    data += b' ' * (16 - (len(data) % 16))
                enc = new.encrypt(data)
                f2.write(enc)
            f2.close()
        f1.close()
    print("mission completed successfully\n")


def AES_dec_files(file_name, key, iv):
    with open(file_name, 'rb') as f1:
        new = AES.new(key, AES.MODE_CBC, iv)
        new_file = input("write the complete path where you want to save file with the extension: ")
        read_size = 1024
        file_size = int(f1.read(16).decode('ascii').lstrip('0'))
        with open(new_file, 'wb') as f2:
            while True:
                data = f1.read(read_size)
                if len(data) == 0:
                    break
                decrypt = new.decrypt(data)
                f2.write(decrypt)
            f2.truncate(file_size)
            f2.close()
        f1.close()
    print("mission completed successfully\n")


def ARC4_enc_message(message, key):
    if len(message) % 16 != 0:
        message += b' ' * (16 - (len(message) % 16))

    new = ARC4.new(key)
    enc = new.encrypt(message)
    encoding = base64.b64encode(enc)
    print("\n #|>#|># your Encrypted message: ", codecs.decode(encoding, 'utf-8'), "\n")


def ARC4_dec_message(message, key):
    dec = base64.b64decode(message)
    new = ARC4.new(key)
    dy = new.decrypt(dec)
    encoding = codecs.decode(dy, 'utf-8')
    print("\n #<|#<|# your Decrypted message: ", encoding, "\n")


def ARC4_enc_files(file_name, key):
    file_size = str(os.path.getsize(file_name)).zfill(16).encode('ascii')
    new_file = input("write the complete path where you want to save the file with the extension: ")
    read_size = 1024
    new = ARC4.new(key)
    with open(file_name, 'rb') as f1:
        with open(new_file, 'wb') as f2:
            f2.write(file_size)
            while True:
                data = f1.read(read_size)
                if len(data) == 0:
                    break
                elif len(data) % 16 != 0:
                    data += b' ' * (16 - (len(data) % 16))
                enc = new.encrypt(data)
                f2.write(enc)
            f2.close()
        f1.close()
    print("mission completed successfully\n")


def ARC4_dec_files(file_name, key):
    with open(file_name, 'rb') as f1:
        new = ARC4.new(key)
        new_file = input("write the complete path where you want to save file with the extension: ")
        read_size = 1024
        file_size = int(f1.read(16).decode('ascii').lstrip('0'))
        with open(new_file, 'wb') as f2:
            while True:
                data = f1.read(read_size)
                if len(data) == 0:
                    break
                decrypt = new.decrypt(data)
                f2.write(decrypt)
            f2.truncate(file_size)
            f2.close()
        f1.close()
    print("mission completed successfully\n")


def DES3_enc_message(message, key, iv):
    if len(message) % 16 != 0:
        message += b' ' * (16 - (len(message) % 16))

    new = DES3.new(key, DES3.MODE_CBC, iv)
    enc = new.encrypt(message)
    encoding = base64.b64encode(enc)
    print("\n #|>#|># your Encrypted message: ", codecs.decode(encoding, 'utf-8'), "\n")


def DES3_dec_message(message, key, iv):
    dec = base64.b64decode(message)
    new = DES3.new(key, DES3.MODE_CBC, iv)
    dy = new.decrypt(dec)
    encoding = codecs.decode(dy, 'utf-8')
    print("\n #<|#<|# your Decrypted message: ", encoding, "\n")


def DES3_enc_files(file_name, key, iv):
    new_file = input("write the complete path where you want to save the file with the extension: ")
    read_size = 1024
    new = DES3.new(key, DES3.MODE_CBC, iv)
    with open(file_name, 'rb') as f1:
        with open(new_file, 'wb') as f2:
            while True:
                data = f1.read(read_size)
                if len(data) == 0:
                    break
                elif len(data) % 16 != 0:
                    data += b' ' * (16 - (len(data) % 16))
                enc = new.encrypt(data)
                encode = base64.b64encode(enc)
                f2.write(encode)
            f2.close()
        f1.close()
    print("mission completed successfully\n")


def DES3_dec_files(file_name, key, iv):
    new = DES3.new(key, DES3.MODE_CBC, iv)
    new_file = input("write the complete path where you want to save the file with the extension: ")
    read_size = 1024
    with open(file_name, 'rb') as f1:
        with open(new_file, 'wb') as f2:
            while True:
                data = f1.read(read_size)
                decode = base64.b64decode(data)
                if len(data) == 0:
                    break
                decrypt = new.decrypt(decode)
                f2.write(decrypt)
            f2.close()
        f1.close()
    print("mission completed successfully\n")


def random():
    print("key == ", binascii.hexlify(os.urandom(8)).decode('utf-8'))
    print("iv == ", binascii.hexlify(os.urandom(8)).decode('utf-8'), "\n")


while True:
    x = input("[H] >> help\n[1] >> file\n[2] >> message\n[3] >> generate random key & iv\n[0] >> exit\n choose:  ")
    if x == 'exit' or x == '0':
        print("\n[ Thanks for your time ^_^ BYE, ]")
        break

    # ==============================================================================================================
    # Encryption and Decryption of messages

    elif x == 'message' or x == '2':
        print("\n1-  AES\n2-  ARC4\n3-  DES3\n4-  CEASER")
        y = int(input("\nwrite the number of the cipher : "))

    # AES-Cipher
    # ------------------------------------------

        if y == 1:
            a = input("write 'E' for AES-Encryption or 'D' for AES-Decryption: ")
            if a == 'E':
                m = codecs.encode(input("write the message: "), 'utf-8')
                while True:
                    k = codecs.encode(input("write your key: "), 'utf-8')
                    v = codecs.encode(input("write your iv: "), 'utf-8')
                    try:
                        AES_enc_messege(m, k, v)
                        break
                    except ValueError:
                        print(" [XXX]/\/\ Wrong in key or iv size, they must be 16 size or 32 or 64 or 128")
            elif a == 'D':
                m = codecs.encode(input("write the Decrypted message: "), 'utf-8')
                while True:
                    k = codecs.encode(input("write your key: "), 'utf-8')
                    v = codecs.encode(input("write your iv: "), 'utf-8')
                    try:
                        AES_dec_message(m, k, v)
                        break
                    except ValueError:
                        print(" [XXX]/\/\ Wrong in key or iv size, they must be 16 size or 32 or 64 or 128")
    # --------------------------------------------------------------------------------------------------

    # ARC4-Cipher
    # ------------------------------------------

        elif y == 2:
            a = input("write 'E' for ARC4-Encryption or 'D' for ARC4-Decryption: ")
            if a == 'E':
                m = codecs.encode(input("write the message: "), 'utf-8')
                while True:
                    k = codecs.encode(input("write your key: "), 'utf-8')
                    try:
                        ARC4_enc_message(m, k)
                        break
                    except ValueError:
                        print(" [XXX]/\/\ Wrong in key >> ARC4 key size must be greater than 8 byte ")
            elif a == 'D':
                m = codecs.encode(input("write the Decrypted message: "), 'utf-8')
                while True:
                    k = codecs.encode(input("write your key: "), 'utf-8')
                    try:
                        ARC4_dec_message(m, k)
                        break
                    except ValueError:
                        print(" [XXX]/\/\ Wrong in key >> ARC4 key size must be greater than 8 byte ")
    # -------------------------------------------------------------------------------------------------

    # DES3-Cipher
    # --------------------------------------------

        elif y == 3:
            a = input("write 'E' for DES3-Encryption or 'D' for DES3-Decryption: ")
            if a == 'E':
                m = codecs.encode(input("write the message: "), 'utf-8')
                while True:
                    k = codecs.encode(input("write your key: "), 'utf-8')
                    v = codecs.encode(input("write your iv: "), 'utf-8')
                    try:
                        DES3_enc_message(m, k, v)
                        break
                    except ValueError:
                        print(" [XXX]/\/\ Wrong in key or iv >> DES3 key must be 16 or 24 bytes & iv must be 8 bytes")
            elif a == 'D':
                m = codecs.encode(input("write the Decrypted message: "), 'utf-8')
                while True:
                    k = codecs.encode(input("write your key: "), 'utf-8')
                    v = codecs.encode(input("write your iv: "), 'utf-8')
                    try:
                        DES3_dec_message(m, k, v)
                        break
                    except ValueError:
                        print(" [XXX]/\/\ Wrong in key or iv >> DES3 key must be 16 or 24 bytes & iv must be 8 bytes")
    # ---------------------------------------------------------------------------------------------------

    # CEASER-cipher
    # ----------------------------------------------

        elif y == 4:
            a = input("write 'E' for CEASER-Encryption or 'D' for CEASER-Decryption: ")
            if a == 'E':
                m = input("write the message: ")
                k = int(input("write your key: "))
                ceaser_enc(m, k)
            elif a == 'D':
                m = input("write the cipher message: ")
                k = int(input("write your key: "))
                ceaser_dec(m, k)
        else:
            print("wrong choose, please choose again")
            continue

    # =====================================================================================================================
    # Encryption and Decryption of files

    elif x == 'file' or x == '1':
        print("1-  AES\n2-  ARC4\n3-  DES3")
        y = int(input("write the number of the cipher : "))

    # AES-Cipher
    # ------------------------------------------

        if y == 1:
            a = input("write 'E' for AES-Encryption or 'D' for AES-Decryption: ")
            if a == 'E':
                while True:
                    try:
                        m = input("write the path of the file: ")
                        k = codecs.encode(input("write your key: "), 'utf-8')
                        v = codecs.encode(input("write your iv: "), 'utf-8')
                        AES_enc_files(m, k, v)
                        break
                    except ValueError:
                        print(" [XXX]/\/\ Wrong in key or iv size, they must be 16 size or 32 or 64 or 128")
                    except FileNotFoundError:
                        print("  [ ... sorry, file not found ... ] ")
            elif a == 'D':
                while True:
                    try:
                        m = input("write the path of the file: ")
                        k = codecs.encode(input("write your key: "), 'utf-8')
                        v = codecs.encode(input("write your iv: "), 'utf-8')
                        AES_dec_files(m, k, v)
                        break
                    except ValueError:
                        print(" [XXX]/\/\ Wrong in key or iv size, they must be 16 size or 32 or 64 or 128")
                    except FileNotFoundError:
                        print("  [ ... sorry, file not found ... ] ")
    # -----------------------------------------------------------------------------------

    # ARC4-Cipher
    # ------------------------------------------

        elif y == 2:
            a = input("write 'E' for ARC4-Encryption or 'D' for ARC4-Decryption: ")
            if a == 'E':
                while True:
                    try:
                        m = input("write the path of the file: ")
                        k = codecs.encode(input("write your key: "), 'utf-8')
                        ARC4_enc_files(m, k)
                        break
                    except ValueError:
                        print(" [XXX]/\/\ Wrong in key >> ARC4 key size must be greater than 8 byte ")
                    except FileNotFoundError:
                        print("  [ ... sorry, file not found ... ] ")
            elif a == 'D':
                while True:
                    try:
                        m = input("write the path of the file: ")
                        k = codecs.encode(input("write your key: "), 'utf-8')
                        ARC4_dec_files(m, k)
                    except ValueError:
                        print(" [XXX]/\/\ Wrong in key >> ARC4 key size must be greater than 8 byte ")
                    except FileNotFoundError:
                        print("  [ ... sorry, file not found ... ] ")
    # ------------------------------------------------------------------------------

    # DES3-Cipher
    # --------------------------------------------

        elif y == 3:
            a = input("write 'E' for DES3-Encryption or 'D' for DES3-Decryption: ")
            if a == 'E':
                while True:
                    try:
                        m = input("write the path of the file: ")
                        k = codecs.encode(input("write your key: "), 'utf-8')
                        v = codecs.encode(input("write your iv: "), 'utf-8')
                        DES3_enc_files(m, k, v)
                    except ValueError:
                        print(" [XXX]/\/\ Wrong in key or iv >> DES3 key must be 16 or 24 bytes & iv must be 8 bytes")
                    except FileNotFoundError:
                        print("  [ ... sorry, file not found ... ] ")
            elif a == 'D':
                while True:
                    try:
                        m = input("write the path of the file: ")
                        k = codecs.encode(input("write your key: "), 'utf-8')
                        v = codecs.encode(input("write your iv: "), 'utf-8')
                        DES3_dec_files(m, k, v)
                    except ValueError:
                        print(" [XXX]/\/\ Wrong in key or iv >> DES3 key must be 16 or 24 bytes & iv must be 8 bytes")
                    except FileNotFoundError:
                        print("  [ ... sorry, file not found ... ] ")
        else:
            print("wrong choose, please choose again")
            continue
    # --------------------------------------------------------------------------------

    # generating random key and iv
    # -----------------------------------------------------

    elif x == 'generate' or x == '3':
        random()
    # --------------------------------------------------------------------------------

    # HELP section
    # -------------------------------------------------------

    elif x == 'help' or x == 'H':
        banner(text)
        print("# ROCKY tool for Encryption/Decryption messages or files\nCreated by: EXZANDAR")
        print("# NOTES: \n\n* this tool use BASE64 encoding and decoding \n** the 'KEY' & 'IV' should be % 16 == 0 "
              "\n*** when you use DES3 Cipher the 'IV' size is '8' "
              "\n**** when you encrypt/decrypt file, write the file with its extension\n"
              "*** you can generate random key &"
              " iv to use them\n** when you use CEASER cipher in Encrypt/Decrypt messages the valid range key [0:25]\n"
              "* you "
              "can send me feedback at hema66458@gmail.com\n")
        print("# EXAMPLE: 'of encryption/decryption messages using AES Cipher' "
              "\nmessage: 'hello world' key: '1234567891234567' iv: '9876543219876543' ")
        print(
            "\n# EXAMPLE: 'of encryption/decryption file using AES cipher'\nfile path: F:\\file.txt\n"
            "key: '1234567891234567'"
            "\niv: '9876543219876543'")
        print(" >>> the encrypted message will be look like 'e3vtzoQyySWdanELjYV2Ng==' <<< ")
        print("\n[ finally hope you use it carefully ]\n")
        banner(text)
    else:
        print("wrong choose, please choose again")
        continue
    # -----------------------------------------------------------------------------
