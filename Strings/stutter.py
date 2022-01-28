def stutter(string):
    copied = ""
    for i in string:
        for j in range(2):
            copied = "".join([copied, i])
    return copied

if __name__=="__main__":
    print(stutter(input("input string: ")))