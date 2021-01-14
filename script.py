import pcrypt
import getpass

# get password from user input in hidden mode using getpass module 
pass_word = getpass.getpass("Enter your password : ")

# encrypt the password and store it in variable
encrypted_password = pcrypt.crypt(pass_word , pcrypt.METHOD_SHA256 , rounds = 50000)

print("*********************************your password is encrypted*******************************")

print("\n")
print(encrypted_password) 