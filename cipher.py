import string

text = input("Please Enter a Statement to Be Encrypted: ")
text = text.lower()
shift = 5


alpha = string.ascii_lowercase
shifted = alpha[shift:] + alpha[:shift]
table = str.maketrans(alpha, shifted)

encrypted = text.translate(table)

print("The Encrypted Statement is: ")

print(encrypted)
