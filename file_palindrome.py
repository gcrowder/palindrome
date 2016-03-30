import sys
import os
import re

def data_munge(path):
    palindromes = open(path, 'r')
    list_of_palindromes = palindromes.readlines()
    return list_of_palindromes

def reverse_string(text):
    if len(text) == 0:
         return ''
    else:
        return reverse_string(text[1:]) + text[0]

def is_palindrome(sentence):
    string = sentence.lower()
    pattern = r'[^A-Za-z]'
    maybe_palindrome = re.sub(pattern, '', string)
    backwards_maybe_drome = reverse_string(maybe_palindrome)
    if maybe_palindrome == backwards_maybe_drome:
        return True
    else:
        return False


def result(boolean):
    if boolean:
        print("Congratulations. Your input is a palindrome.")
    else:
        print("I'm sorry. Your input is not a palindrome.")

def main(path):
    if os.path.exists(path):
        the_list = data_munge(path)
        for line in the_list:
            result(is_palindrome(line))




if __name__ == '__main__':
    if len(sys.argv) > 1: # If the user actually gave the path of a file when calling the program
        main(sys.argv[1]) #grab the path of that file. sys.argv[0] is the program itself
    else:
        sys.exit(1) #if no file, exit with an error
    sys.exit(0) #everything worked great. exit sucessfully
