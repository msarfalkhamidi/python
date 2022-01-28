def start_end_letter(char):
    print('Looking for two "'+char+'" words in a row.')
    word = ""
    count = 0
    while count < 2:
        string = input("Type a word: ")
        char1 = char.lower()
        string1 = string.lower()
        if string1.startswith(char1) and string1.endswith(char1):
            word = string
            count = count + 1
        else:
            count = 0
    print('"'+char+'" is for "'+word+'"')

if __name__=="__main__":
    start_end_letter(input("start end letter with: "))