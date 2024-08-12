BaseEncryptionDecryption = 'abcdefghijklmnopqrstuvwxyz.*/!?.*%^@|()é&²=)àç_-'
Lengthofthebase = len(BaseEncryptionDecryption)

def encrypt_decrypt(text, encryptordecrypt, key):
    result=''
    if encryptordecrypt == 'd':
        key = -key
    
    for letter in text : 
        letter = letter.lower()
        if not letter == ' ':
            index = BaseEncryptionDecryption.find(letter)
            if index == -1:
                result += letter
            else:
                new_index = index + key
                if new_index >=Lengthofthebase :
                    new_index -= Lengthofthebase
                elif new_index < 0 :
                    new_index += Lengthofthebase
                result += BaseEncryptionDecryption[new_index]
    return result


print()
print('***** CAESAR CIPHER PROGRAM *****')
print()

print('Do you want to encrypt or decrypt?')
UserPreference = input('e/d: ').lower()
print()

if UserPreference == 'e':
    print('ENCRYPTION MODE SELECTED')
    print()
    
    while True:
        try:
            key = int(input(f'Enter the key (1 through {Lengthofthebase}): '))
            break
        except ValueError:
            print('INVALID: you need to enter a number!')
    while True:
        texttoencryptordecrypt = input('Enter the text to encrypt: ')
        if not texttoencryptordecrypt.strip():
            print('INVALID: you need to enter a string!')
        else:
            break
    ciphertext = encrypt_decrypt(texttoencryptordecrypt, UserPreference, key)
    print(f'CIPHERTEXT: {ciphertext}')


elif UserPreference == 'd' :
    print('DECRYPTION MODE SELECTED')
    print()

    while True:
        try:
            key = int(input(f'Enter the key (1 through {Lengthofthebase}): '))
            break
        except ValueError:
            print('INVALID: you need to enter a number!')
    while True:
        texttoencryptordecrypt = input('Enter the text to decrypt: ')
        if not texttoencryptordecrypt.strip():
            print('INVALID: you need to enter a string!')
        else:
            break
    originaltext = encrypt_decrypt(texttoencryptordecrypt, UserPreference, key)
    print(f'ORIGINALTEXT: {originaltext}')