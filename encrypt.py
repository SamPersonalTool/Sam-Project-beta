from cryptography.fernet import Fernet 
##Generate a random encryption key 
key = Fernet.generate_key()

with open('key.key', 'wb') as file: 
    file.write(key)

##Load the encryption key from the file
with open('key.key', 'rb') as file: 
    key = file.read() 

##Encrypt the API key
api_key = b'your_api_key' 
fernet = Fernet(key) 
encrypted_api_key = fernet.encrypt(api_key)

with open('encrypted_api_key.txt', 'wb') as file: 
    file.write(encrypted_api_key)