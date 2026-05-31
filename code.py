import sys

def bruteforce(letter, rot):
    # space == 32
    if ord(letter) == 32:
        return 32
    # numbers are between 48 and 57
    elif ord(letter) >= 48 and ord(letter) <= 57:
        return ord(letter)
    # capital letters are between 65 and 90
    elif ord(letter) >= 65 and ord(letter) <= 90:
        i = ord(letter) - 65 # subtract 65 so A = 0
        return ((i - rot) % 26) + 65 # add back 65 to get ascii
    # lowercase letters are between 97 and 122
    elif ord(letter) >= 97 and ord(letter) <= 122:
        i = ord(letter) - 97 # subtract 97 so a = 0
        return ((i - rot) % 26) + 97 # add back 97 to get ascii

if len(sys.argv) < 2:
    print("Enter the ciphertext to be decoded as an argument.")
    exit(1)
elif len(sys.argv) > 2:
    print("There should only be one ciphertext. Enclose your message in quotes if there are spaces.")
    exit(1)
else:
    text = sys.argv[1]

for i in range(0, 26):
    print(f"{i}: ", end='')

    for letter in text:
        print(chr(bruteforce(letter, i)), end='')

    print("\n")
