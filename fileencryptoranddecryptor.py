from cryptography.fernet import Fernet
import os 

class EncryptYourFiles:

    def __init__(self, PATH):

        self.PATH = PATH

    def make_key(self):

        k = Fernet.generate_key()

        global key
        key = Fernet(k)

    def go_to_directory(self):

        os.chdir(PATH)

        # print(os.listdir())

    def encrypt(self):

        for filename in os.listdir(os.getcwd()):
            
            with open(os.path.join(os.getcwd(), filename), 'r') as f: 

                data = f.read().encode()

            with open(os.path.join(os.getcwd(), filename), 'wb') as same_file: 

                encrypted = key.encrypt(data)

                same_file.truncate(0)

                same_file.write(encrypted)

                # print(encrypted.decode())

    def decrypt(self):

        for filename in os.listdir(os.getcwd()):

            with open(os.path.join(os.getcwd(), filename), 'rb') as f: 

                contents = f.read()
    
            with open(os.path.join(os.getcwd(), filename), 'wb') as f: 
                
                decrypted = key.decrypt(contents)

                decrypted.decode()

                f.write(decrypted)

                # print(decrypted.decode())

PATH = "your_path_to_file_or_files"

encryptor = EncryptYourFiles(PATH)

encryptor.make_key()
encryptor.go_to_directory()
encryptor.encrypt()
encryptor.decrypt()
