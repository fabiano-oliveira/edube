import typing

"""
You are already familiar with the Caesar cipher, and this is why we want you to improve the code we showed you recently.

The original Caesar cipher shifts each character by one: a becomes b, z becomes a, and so on. Let's make it a bit harder, and allow the shifted value to come from the range 1..25 inclusive.

Moreover, let the code preserve the letters' case (lower-case letters will remain lower-case) and all non-alphabetical characters should remain untouched.

Your task is to write a program which:

asks the user for one line of text to encrypt;
asks the user for a shift value (an integer number from the range 1..25 - note: you should force the user to enter a valid shift value (don't give up and don't let bad data fool you!)
prints out the encoded text.
"""

def cipher(message: str, shift: int) -> str:
    ciphered_message = ""

    for c in message:
        if c.isalpha():
            low_bound = ord("A") if c.isupper() else ord("a")
            high_bound = ord("Z") if c.isupper() else ord("z")

            ciphered = ord(c) + shift
            if ciphered > high_bound:
                ciphered = ciphered - high_bound - 1 + low_bound
            ciphered_message += chr(ciphered)
        else:
            ciphered_message += c
        
    return ciphered_message


message = input("Enter the message to cipher: ")
shift_len = None

while shift_len is None:
    try:
        shift_len = int(input("Enter shift value between 1 and 25: "))
        if(shift_len < 1 or shift_len > 25):
            shift_len = None
            print("Enter a valid shift value!")
    except ValueError:
        print("Invalid number!")
        shift_len = None
        
print("Original message:", message)
print("shift:", shift_len)
print("Ciphered message:", cipher(message, shift_len))