def convert_to_alt_caps(string):
    string = string.lower()
    converted = ""
    j = 0
    for i in range(len(string)):
        if string[i] != " ":
            j = j+1
        if j%2 != 1:
            converted = converted + string[i].upper()
        else:
            converted = converted + string[i]
    return converted

if __name__=="__main__":
    print(convert_to_alt_caps(input("input string: ")))