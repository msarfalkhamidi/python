def second_half_letters(string):
    filtered = ""
    for i in string:
        if "N" <= i <= "Z" or "n" <= i <= "z":
            filtered = "".join([filtered, i])
    return len(filtered)

if __name__=="__main__":
    print(second_half_letters(input("input a word: ")))