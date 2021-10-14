lettres = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

def alphaDec_lettre(lettres,lettre):
    index_lettre = lettres.find(lettre)
    new_lettres = lettres[index_lettre:] +  lettres[:index_lettre]
    return new_lettres
def litsalpha(lettre,key):
    l = []
    for c in key:
        l.append(alphaDec_lettre(lettres,c))
    return l

msg = input("enter a message: ")
key = input("enter a key: ")

def cryptmsg(msg,key):
    encrypted = ""
    k = 0
    l = litsalpha(lettres,key)
    for c in  msg:
        pos = lettres.index(c)
        crypted_char = l[k][pos]
        encrypted += crypted_char
        k = (k+1) % len(l)
    return encrypted


print(cryptmsg(msg,key))
