import tea

if __name__ == '__main__':
    key = "1122334455667788".encode()
    origin = bytearray()

    for i in range(16):
        origin.append(i)

    print('原数据:  ', origin.hex())
    encrypt_data = tea.encrypt(origin, key)
    print('加密数据:', encrypt_data.hex())
    decrypt_data = tea.decrypt(encrypt_data, key)
    print('解密数据:', decrypt_data.hex())
