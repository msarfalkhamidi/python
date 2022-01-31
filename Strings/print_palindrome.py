def print_palindrome():
    string = input("Type one or more words: ")
    lower = string.lower()
    size = len(string)
    check = False
    i = 0 
    j = int(size/2)
    while i < j:
        if lower[i] == lower[size-1-i]:
            check = True
        else:
            check = False
            break
        i = i+1
    if check == True:
        print(string, "is a palindrome!")
    else:
        print(string, "is not a palindrome.")

if __name__ =="__main__":
    print_palindrome()