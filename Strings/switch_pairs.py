def switch_pairs(string):
    switched = ""
    i = 0
    while i < len(string):
        if (i+1) < len(string):
            switched = "".join([switched, string[i+1]])
        switched = "".join([switched, string[i]])
        i = i+2
    return switched

if __name__=="__main__":
    string = input("input string: ")
    print(switch_pairs(string))