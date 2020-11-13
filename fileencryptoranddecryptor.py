from cryptography.fernet import Fernet
import os
from datetime import datetime

date = datetime.now().date()
k = Fernet.generate_key()

key = Fernet(k)

class EncryptYourFiles:

    def __init__(self, PATH):

        self.PATH = PATH

    def save_key(self):

        key_file = open(f"key{date}.key", "wb")
        key_file.write(k)
        key_file.close()

    def encrypt_file(self):

        os.chdir(PATH)
        print(os.listdir())
        
        with open(PATH, "r") as f:

            data = f.read().encode()

        with open(PATH, "wb") as same_file:

            encrypted = key.encrypt(data)

            same_file.truncate(0)

            same_file.write(encrypted)

    def decrypt_file(self):

        with open(PATH, 'rb') as f: 

            data = f.read()
    
        with open(PATH, 'wb') as f: 
            
            decrypted = key.decrypt(data)

            decrypted.decode()

            f.write(decrypted)

            #print(decrypted.decode())

    def encrypt_directory(self):
        
        os.chdir(PATH)
        print(os.listdir())

        for filename in os.listdir(os.getcwd()):
            
            with open(os.path.join(os.getcwd(), filename), 'r') as f: 

                data = f.read().encode()

            with open(os.path.join(os.getcwd(), filename), 'wb') as same_file: 

                encrypted = key.encrypt(data)

                same_file.truncate(0)

                same_file.write(encrypted)

                print(encrypted.decode())

    def decrypt_directory(self):

        for filename in os.listdir(os.getcwd()):

            with open(os.path.join(os.getcwd(), filename), 'rb') as f: 

                contents = f.read()
    
            with open(os.path.join(os.getcwd(), filename), 'wb') as f: 
                
                decrypted = key.decrypt(contents)

                decrypted.decode()

                f.write(decrypted)

                print(decrypted.decode())

# Change this to the path of the individual file or directory
PATH = "your_path_to_files_or_files"

encryptor = EncryptYourFiles(PATH)

choice = input("Would you like to encrypt a file or a directory (that can include sub-directories)")

if choice.lower() == "file":

    encryptor.save_key()
    encryptor.go_to_directory(
    encryptor.encrypt_file()
    # encryptor.decrypt_file()

elif choice.lower() == "directory":

    encryptor.save_key()
    encryptor.encrypt_directory()
    encryptor.decrypt_directory()

else:
    print("Invalid Input.")
