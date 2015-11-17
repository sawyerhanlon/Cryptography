"""
cryptography.py
Author: <your name here>
Credit: <list sources used, if any>

Assignment:

Write and submit a program that encrypts and decrypts user data.

See the detailed requirements at https://github.com/HHS-IntroProgramming/Cryptography/blob/master/README.md
"""
def evenstrings(message, key):
    messlen = len(message)
    keylen = len(key)
    if keylen < messlen:
        modkey1 = (messlen // keylen)*key
        modkey2 = key[(messlen % keylen)-1]
        return modkey1 + modkey2
    elif keylen == messlen:
        return key
    else:
        return key[messlen]
a = True
while a:
    command = str(input("Enter e to encrypt, d to decrypt, or q to quit: "))
    if command != "q":
        associations = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789 .,:;'\"/\\<>(){}[]-=_+?!"
        message = str(input("Message: "))
        key = str(input("Key: "))
        elist = []
        if command == "e":
            modkey = evenstrings(message, key)
            b = True
            while True:
                x = len(modkey)
                elist.append(modkey[x])
                x -= 1
                if x == 0:
                    b = False
                
    

        elif command == "d":
            print("")

    elif command == "q":
        print("Goodbye!")
        a = False
    else:
        print("Did not understand command, try again.")