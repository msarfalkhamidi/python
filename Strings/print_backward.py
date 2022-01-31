def print_backward(string):
    backwarded = ""
    index = len(string)
    while index > 0:
        backwarded = backwarded + string[index-1]
        index = index - 1
    print(backwarded) 

if __name__=="__main__":
    print_backward(input("input string: "))