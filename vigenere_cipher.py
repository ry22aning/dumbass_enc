uppercase = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
lowercase = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
def vigenere_cipher(plainText, key):
    key_length = len(key)
    key_index = 0
    cryptText = []

    for eachLetter in plainText:
        if eachLetter in uppercase:
            index = uppercase.index(eachLetter)
            indexKey = lowercase.index(key[key_index % key_length]) #This part ensures the index stays within the bounds of the key, even if key_index exceeds the length of the key.

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

        #outText.append(fstep(cryptText))   
    #return ''.join(cryptText)
    #return ''.join(outText)
    


def fstep(cryptText, key_length):
    outText = []

    for char in cryptText:
        if char in uppercase:
            char_set = uppercase
        elif char in lowercase:
            char_set = lowercase
        else:
            outText.append(char)
            continue

        index = char_set.index(char)
        finalIndex = (index + key_length) % 26 
        outText.append(char_set[finalIndex])

    return ''.join(outText)


#Input from user
plainText = input("Enter the text: ")
key = input("Enter the key: ")

if key != 'quantum':  # Only proceed if the key is correct
    print("Invalid key")
else:
    key = key.lower()  # Normalize the key to lowercase

# Function call
encryptedText = vigenere_cipher(plainText, key)
print("Encrypted Text:",''.join( encryptedText))
#final call
finalOutput = fstep(encryptedText, len(key))
print("Finalprocessed encryption: ", finalOutput)
