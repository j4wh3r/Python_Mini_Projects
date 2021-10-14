message = input("enter a message: ")


alpha = "abcdefghijklmnopqrstuvwxyz"

def codageROT13(m):
    secret = ""
    l = []
    for i in m:
        if i.isalpha():
            sec = (alpha.find(i) +13) % 26
            l.append(alpha[sec])
        else:
            l.append(i)
    encoded = ''.join(l)
    return encoded

# def decodageROT(encoded):
#     l = []
#     for i in encoded:
#         if i.isalpha():
#             dec = (alpha.find(i) - 13) % 26
#             l.append(alpha[dec])
#         else:
#             l.append(i)
#     decoded = ''.join(l)
#     return decoded


def decodageROT(encoded):
    return codageROT13(encoded)

encoded = codageROT13(message)
decoded = decodageROT(encoded)

print(encoded)
print(decoded)

