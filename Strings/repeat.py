def repeat(string, number):
    repeated = ""
    for i in range(number):
        repeated = repeated + string
        i = i+1
    return repeated

if __name__=="__main__":
    print(repeat(input("input string: "), int(input("repetition: "))))