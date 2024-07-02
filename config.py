from cryptography.fernet import Fernet
#Load the key from the file
def load_key():
    with open('key.key', 'rb') as file:        
        key = file.read()
        return key
key = load_key()
#Decrypt a string
def decrypt_string(encrypted_string, key):    
    f = Fernet(key)
    decrypted_string = f.decrypt(encrypted_string).decode()    
    return decrypted_string
#Load the encrypted API key and decrypt it
with open('encrypted_api_key.txt', 'rb') as file:    
    encrypted_api_key = file.read()
decrypted_api_key = decrypt_string(encrypted_api_key, key)