def is_palindrome(word):
    if len(word) <= 0:
        return True
    elif (first(word) == last(word)) and (is_palindrome(middle(word))):
        return True
    else:
        return False
    
def first(word):
    return word[0]

def last(word):
    return word[-1]

def middle(word):
    return word[1:-1]

def test():
    print(middle("abc"))
    print(middle("ab"))
    print(middle("a"))
    print(middle(""))
    print(is_palindrome("noon"))
    print(is_palindrome("redivider"))
    print(is_palindrome("murugavel"))
    print(is_palindrome("malayalam"))

test()
