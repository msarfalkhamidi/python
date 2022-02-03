def caesar_chiper(string, shift):
    library = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
    encoded = ""
    string = string.upper()
    for i in string:
        if i in library:
            index = library.index(i)
            index = index + shift
            if index > 25 or index < -25:
                index = index % 26
            encoded = encoded + library[index]
        else:
            encoded = encoded + i
    return encoded

if __name__=="__main__":
    print(caesar_chiper(input("Your message? "), int(input("Encoding key? "))))