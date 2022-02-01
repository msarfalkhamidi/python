import math

def is_palindrome(string):
    string = string.lower()
    check = False
    i = 0
    if len(string) == 0 or len(string) == 1:
        check = True
    else:
        while i < math.floor(len(string)/2):
            if string[i] == string[len(string)-1-i]:
                check = True
            else:
                check = False
                break
            i = i+1
    return check

if __name__=="__main__":
    print("palindrome?", is_palindrome(input("input string: ")))