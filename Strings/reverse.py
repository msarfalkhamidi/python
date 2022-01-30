def reverse(string):
    reversed = ""
    i = len(string)
    while i > 0:
        reversed = reversed + string[i-1]
        i = i-1
    return reversed

if __name__=="__main__":
    print("reversed:", reverse(input("input string: ")))