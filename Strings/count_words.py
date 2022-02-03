def count_words(string):
    splited = string.split()
    return len(splited)

if __name__=="__main__":
    print("words:", count_words(input("input string: ")))