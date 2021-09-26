
def ispalindrome(sentence):
    sentence = sentence.lower()
    i = 0
    j = len(sentence) - 1
    result = True

    while i <= j and result:
        while not sentence[i].isalpha() and i <= j:
            i += 1
        while not sentence[j].isalpha() and i <= j:
            j -= 1

        if sentence[i] != sentence[j]:
            result = False
        else:
            i += 1
            j -= 1
    
    return result
 

def print_if_is_palindrome(sentence):
    if(ispalindrome(sentence)):
        print(repr(sentence), "is a palindrome.")
    else:
        print(repr(sentence), "is not a palindrome.")

print_if_is_palindrome("Ten animals I slam in a net.")
print_if_is_palindrome("Eleven animals I slam in a net")