import re

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


def user_input():
    try:
        sentence = input("Please enter a word or a sentence. ")
    except:
        print("That did not work. Please run program again.")
        exit()
    else:
        return sentence

def result(boolean):
    if boolean:
        print("Congratulations. Your input is a palindrome.")
    else:
        print("I'm sorry. Your input is not a palindrome.")

def main():
    the_string = user_input()
    result(is_palindrome(the_string))




if __name__ == '__main__':
    main()
