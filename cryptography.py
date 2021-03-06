"""
cryptography.py
Author: Sawyer Hanlon
Credit: Morgan Melliment

Assignment:

Write and submit a program that encrypts and decrypts user data.

See the detailed requirements at https://github.com/HHS-IntroProgramming/Cryptography/blob/master/README.md
"""
def evenstrings(message, key):
    messlen = len(message)
    keylen = len(key)
    if keylen < messlen:
        modkey1 = (messlen // keylen)*key
        modkey2 = key[0:(messlen % keylen)]
        return modkey1 + modkey2
    elif keylen == messlen:
        return key
    else:
        return key[0:messlen]
a = True
while a:
    command = input("Enter e to encrypt, d to decrypt, or q to quit: ")
    associations = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789 .,:;'\"/\\<>(){}[]-=_+?!"
    elist = []
    elist2 = []
    elist3 = []
    if command == "e":
        message = input("Message: ")
        key = input("Key: ")
        modkey = evenstrings(message, key)
        for a in message:
            messa = associations.find(a)
            elist.append(messa)
        for b in modkey:
            modkeya = associations.find(b)
            elist2.append(modkeya)
        ziplist = list(zip(elist,elist2))
        for z in ziplist:
            if z[0] + z[1] > 84:
                elist3.append((z[0]+z[1]) % 85)
            else:
                elist3.append(z[0]+z[1])
        for c in elist3:
            print(associations[c], end='')
        print('')
    elif command == "d":
        message = input("Message: ")
        key = input("Key: ")
        modkey = evenstrings(message, key)
        for a in message:
            messa = associations.find(a)
            elist.append(messa)
        for b in modkey:
            modkeya = associations.find(b)
            elist2.append(modkeya)
        ziplist = list(zip(elist,elist2))
        for z in ziplist:
            if z[0] - z[1] < 0:
                elist3.append((z[0]-z[1]) + 85)
            else:
                elist3.append(z[0]-z[1])
        for c in elist3:
            print(associations[c], end='')
        print('')
    elif command == "q":
        print("Goodbye!")
        a = False
    else:
        print("Did not understand command, try again.")