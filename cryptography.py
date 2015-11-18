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
        elist2 = []
        if command == "e":
            modkey = evenstrings(message, key)
            for a in message:
                messa = associations.find(a)
                elist.append(messa)
            for b in key:
                keya = associations.find(b)
                elist2.append(b)
            ziplist = zip(elist,elist2)
            print(ziplist)
            
            
            
            
                
    

        elif command == "d":
            print("")

    elif command == "q":
        print("Goodbye!")
        a = False
    else:
        print("Did not understand command, try again.")