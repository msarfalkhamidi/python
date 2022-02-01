def is_rotation(string, string2):
    check = False
    if string == "" and string2 == "":
        check = True
    elif len(string) == len(string2):
        for i in range(len(string)):
            string2 = string2[1:] + string2[0]
            if string == string2:
                check = True
            i = i+1
    return check

if __name__=="__main__":
    print(is_rotation(input("input string: "), input("input string 2: ")))