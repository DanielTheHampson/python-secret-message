from characterlist import chars as c

string = input("input text: ")
key = input("key: ")

doEncrypt = input("encrypt or decrypt (e or d): ")

def encrypt(inText, key):
    inChars = list(inText)
    out = []

    for j in inChars:
        out.append(c[c.index(j.lower())+int(key)])

    outstr = ""
    for ele in out:
        outstr += ele

    print(outstr)
    return outstr

def decrypt(inText, key):
    inChars = list(inText)
    out = []

    for j in inChars:
        out.append(c[c.index(j.lower()) - int(key)])

    outstr = ""
    for ele in out:
        outstr += ele

    print(outstr)
    return outstr

if doEncrypt.lower() == "e":
    encrypt(string, key)
else:
    decrypt(string, key)

input("Press enter to exit.. ")
