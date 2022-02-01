def name_game(name):
    splited = name.split()
    for i in range(len(splited)):
        print_name(splited[i])
        print()

def print_name(string):
    deleted = ""
    i = 1
    while i < len(string):
        deleted = deleted + string[i]
        i = i+1
    print(string + ", " + string + ", bo-B" + deleted)
    print("Banana-fana fo-F" + deleted)
    print("Fee-fi-mo-M" + deleted)
    print(string.upper() + "!")

if __name__=="__main__":
    name_game(input("What is your name? "))