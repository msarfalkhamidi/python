def reverse_word_order(string):
    splited = string.split()
    splited.reverse()
    reversed = ""
    i = 0
    while i < len(splited):
        if i == 0: reversed = splited[i]
        else: reversed = " ".join([reversed, splited[i]])
        i = i + 1
    return reversed

if __name__=="__main__":
    print(reverse_word_order(input("input string: ")))