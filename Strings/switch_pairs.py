import fileinput 

def switch_pairs(string):
    switched = ""
    i = 0
    while i < len(string):
        if (i+1) < len(string):
            x = string[i+1]
            switched = "".join([switched, x])
        x = string[i]
        switched = "".join([switched, x])
        i = i+2
    return switched

if __name__=="__main__":
    string = input("input string: ")
    print(switch_pairs(string))