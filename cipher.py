#Caesar Cipher

import string

text = input("Please Enter a Statement to Be Encrypted: ")
text = text.upper()
shift = 5


alpha = string.ascii_uppercase
shifted = alpha[shift:] + alpha[:shift]
table = str.maketrans(alpha, shifted)

encrypted = text.translate(table)

print(encrypted)
