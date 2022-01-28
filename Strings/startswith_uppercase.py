def startswith_uppercase(string):
    if "A" <= string[0] <= "Z":
        return True
    else:
        return False

if __name__=="__main__":
    result = startswith_uppercase(input("input string: "))
    print("Starts with Uppercase?", result)