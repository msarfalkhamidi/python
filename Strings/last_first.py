def last_first(string):
    name = string.split()
    name = name[1] + ", " + name[0][0] + "."
    return name

if __name__=="__main__":
    print(last_first(input("input name: ")))