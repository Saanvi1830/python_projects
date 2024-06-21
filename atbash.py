# Atbash Ciper Encrypter and Decrypter

def char_to_num(x):
    if x == 'A' or x == 'a':
        return 0
    if x == 'B' or x == 'b':
        return 1
    if x == 'C' or x == 'c':
        return 2
    if x == 'D' or x == 'd':
        return 3
    if x == 'E' or x == 'e':
        return 4
    if x == 'F' or x == 'f':
        return 5
    if x == 'G' or x == 'g':
        return 6
    if x == 'H' or x == 'h':
        return 7
    if x == 'I' or x == 'i':
        return 8
    if x == 'J' or x == 'j':
        return 9
    if x == 'K' or x == 'k':
        return 10
    if x == 'L' or x == 'l':
        return 11
    if x == 'M' or x == 'm':
        return 12
    if x == 'N' or x == 'n':
        return 13
    if x == 'O' or x =='o':
        return 14
    if x == 'P' or x == 'p':
        return 15
    if x == 'Q' or x == 'q':
        return 16
    if x == 'R' or x == 'r':
        return 17
    if x == 'S' or x == 's':
        return 18
    if x == 'T' or x == 't':
        return 19
    if x == 'U' or x == 'U':
        return 20
    if x == 'V' or x == 'v':
        return 21 
    if x == 'W' or x == 'w':
        return 22 
    if x == 'X' or x == 'x':
        return 23 
    if x == 'Y' or x == 'y':
        return 24 
    if x == 'Z' or x == 'z':
        return 25
    
def num_to_char(x):
    if x == 0:
        return 'a'
    if x == 1:
        return 'b'
    if x == 2:
        return 'c'
    if x == 3:
        return 'd'
    if x == 4:
        return 'e'
    if x == 5:
        return 'f'
    if x == 6:
        return 'g'
    if x == 7:
        return 'h'
    if x == 8:
        return 'i'
    if x == 9:
        return 'j'
    if x == 10:
        return 'k'
    if x == 11:
        return 'l'
    if x == 12:
        return 'm'
    if x == 13:
        return 'n' 
    if x == 14:
        return 'o' 
    if x == 15:
        return 'p'
    if x == 16:   
        return 'q' 
    if x == 17:
        return 'r' 
    if x == 18:
        return 's' 
    if x == 19:
        return 't'
    if x == 20:
        return 'u'  
    if x == 21:
        return 'v' 
    if x == 22:
        return 'w'  
    if x == 23:
        return 'x'  
    if x == 24:
        return 'y'  
    if x == 25:
        return 'z' 
cryptographyType = int(input("Enter 1 for encryption and 2 for decryption:"))

if cryptographyType == 1:
    str = input("You have chosen encryption. Please enter your encrypted code:")
    result = ""
    for item in str:
        value = char_to_num(item)
        value = 25 - value
        value = num_to_char(value)
        result = result + value

    print(result)

elif cryptographyType == 2:
    str1 = input("You have chosen decryption. Please enter your decrypted code:")
    result1 = ""
    for x in str1:
        value1 = char_to_num(x)
        value1 = 25 - value1
        value1 = num_to_char(value1)
        result1 = result1 + value1

    print(result1)
