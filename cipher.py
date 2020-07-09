# Code out your function definitions here

# array with alphabet
# define decoder(take in number and message)
#   for loop number in message:
#       return array[message position in array - number]
#

def decoder(num, message):
    alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
    array1 = []
    array2 = []
    for i in message:
        if i in alphabet:
            index = alphabet.index(i)
            crypting = (index + num) % 26
            array1.append(crypting)
            newletter = alphabet[crypting]
            array2.append(newletter)
        return array2

print(decoder(3, "Hello"))
