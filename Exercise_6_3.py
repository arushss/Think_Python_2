def first(word):
    return word[0]

def last(word):
    return word[-1]

def middle(word):
    return word[1:-1]

def is_palindrome(word):

    if len(word)<=1:
        print("Yes")
        return

    if first(word)==last(word):
        return is_palindrome(middle(word))
    else:
        print("No")
        return

is_palindrome("IUPUI")