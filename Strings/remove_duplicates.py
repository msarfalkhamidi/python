def remove_duplicates(string):
    removed = ""
    i = 0
    while i < len(string):
        if i == 0 or string[i] != string[i-1]:
            removed = removed + string[i]
        i = i+1
    return removed

if __name__=="__main__":
    print(remove_duplicates(input("input string: ")))