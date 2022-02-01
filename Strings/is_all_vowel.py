from is_vowel import is_vowel

def is_all_vowels(word):
    check = True
    for i in word:
        if is_vowel(i) == False:
            check = False
            break
    return check

if __name__=="__main__":
    print(is_all_vowels(input("input word: ")))