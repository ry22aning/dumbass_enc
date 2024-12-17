uppercase = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
lowercase = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def vigenere_cipher(plainText, key):
    cryptText = []
    key_length = len(key)
    key_index = 0

    for eachLetter in plainText:
        if eachLetter in uppercase:
            index = uppercase.index(eachLetter)
            indexKey = lowercase.index(key[key_index % key_length])
            new_index = (index + indexKey) % 26
            cryptText.append(uppercase[new_index])
            key_index += 1
        elif eachLetter in lowercase:
            index = lowercase.index(eachLetter)
            indexKey = lowercase.index(key[key_index % key_length])
            new_index = (index + indexKey) % 26
            cryptText.append(lowercase[new_index])
            key_index += 1
        else:
            cryptText.append(eachLetter)
    
    return ''.join(cryptText)

def fstep(cryptText, key=5):
    ledger = lowercase + [' '] + list('1234567890')
    outputText = ""

    for char in cryptText:
        if char in ledger:
            inputIndex = ledger.index(char)
            outputIndex = (inputIndex + key) % len(ledger)
            outputText += ledger[outputIndex]
        else:
            outputText += char  # Keep non-ledger characters unchanged

    return outputText

plainText = input("Enter the text: ")
key = input("Enter the key: ")

if key != 'quantum':  # Only proceed if the key is correct
    print("Invalid key")
else:
    key = key.lower()  # Normalize the key to lowercase
    encryptedText = vigenere_cipher(plainText, key)
    #print("Encrypted Text:", encryptedText)

    # Process the encrypted text through fstep
    finalOutput = fstep(encryptedText)
    print("Final Processed Text (fstep):", finalOutput)
