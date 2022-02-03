def add_commas(string):
    string = reverse(string)
    count = 0
    added = ""
    for i in string:
        count = count + 1
        added = added + i
        if count%3 == 0:
            added = added + ","
    added = reverse(added)
    if len(added) > 0 and added[0] == ",":
        added = added[1:]
    return added

def reverse(string):
    reversed = ""
    i = len(string)
    while i > 0:
        reversed = reversed + string[i-1]
        i = i-1
    return reversed

if __name__=="__main__":
    print(add_commas(input("input numbers: ")))