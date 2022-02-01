import math

def is_palindrome(string):
    string = string.lower()
    check = False
    size = len(string)
    i = 0
    j = math.floor(size/2)
    if len(string) == 0 or len(string) == 1:
        check = True
    else:
        while i < j:
            if string[i] == string[size-1-i]:
                check = True
            else:
                check = False
                break
            i = i+1
    return check

if __name__=="__main__":
    print("palindrome?", is_palindrome(input("input string: ")))