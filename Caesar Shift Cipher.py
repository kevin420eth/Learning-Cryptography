#Affine Cipher
def affine_encrypt(n):
    n = (n*5+3)%26
    return

#Caesar Shift Cipher
def caesar_encrypt(n):
    n = (n+3)%26
    return n

alphabet = "abcdefghijklmnopqrstuvwxyz"

while True:
    original_password = input("Please enter your password:\n").lower()
    if original_password.isalpha() == True:
        break
    else:
        print("Must not include numbers or symbols! Try again!")

new_password = ""

for _ in original_password:
    new_letter = alphabet[caesar_encrypt(alphabet.index(_))]
    new_password += new_letter

print(f"Your new password is {new_password}")

