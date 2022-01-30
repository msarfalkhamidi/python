def remove_all(string, char):
    removed = ""
    for i in string:
        if i != char:
            removed = removed + i
    return removed

if __name__=="__main__":
    print(remove_all(input("input string: "), input("input character: ")))