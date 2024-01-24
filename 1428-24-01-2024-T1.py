def Encryption(n, text):
    result = ""  
    for i in range(len(text)):
        char = text[i]

        if char.isupper():
            result += chr((ord(char) + n - 65) % 26 + 65)
        else:
            result += chr((ord(char) + n - 97) % 26 + 97)

    return result


def Decryption(n,out):
     result1 = ""  
     for i in range(len(out)):
        char2 = out[i]

        if char2.isupper():
            result1 += chr((ord(char2) -n- 65 + 26 ) % 26 + 65)
        else:
            result1 += chr((ord(char2) - n - 97 + 26) % 26 + 97)

     return result1


text = input("Enter a text:")
key = int(input("Enter the Key:"))
out = Encryption(key ,text)

print("Text  : " + text)
print("Shift : " + str(key))
print("Cipher: " + out)
print("decripted:"+Decryption(key,out))
