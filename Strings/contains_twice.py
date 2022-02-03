def contains_twice(string, char):
    check = False
    count = 0
    for i in string:
        if i == char:
            count = count+1
    if count > 1:
        check = True
    return check

if __name__=="__main__":
    string = input("input string: ")
    char = input("input character: ")
    print("There are two or more", char, "in", string, ":", contains_twice(string, char))