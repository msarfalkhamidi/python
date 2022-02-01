def is_vowel(letter):
    check = False
    if letter in ["A", "I", "U", "E", "O", "a", "i", "u", "e", "o"]:
        check = True
    return check

if __name__=="__main__":
    print(is_vowel(input("input letter: ")))