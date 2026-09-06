print("Welcome to the Caesar Cipher!")
print("This program will encrypt a message using the Caesar cipher.")
a=int(input("Enter the shift value (1-25): "))
b=input("Enter the message to encrypt: ")
b=b.lower()
c=""
for i in b:
    if i.isalpha():
        c+=chr((ord(i)-97+a)%26+97)
    else:
        c+=i
print("Encrypted message:", c)
