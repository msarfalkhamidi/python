def name_diamond(string):
    i = 0
    word = ""
    while i < len(string):
        word = word + string[i]
        i = i+1
        print(word)
    i = 0
    for i in range(len(string)-1):
        j = 0
        word = ""
        while j < i+1:
            word = word + " "
            j = j+1
        while j < len(string):
            word = word + string[j]
            j = j+1
        print(word)

if __name__=="__main__":
    name_diamond(input("input string: "))