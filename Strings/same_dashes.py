def same_dashes(str1, str2):
    check = False
    if sum_dashes(str1) == sum_dashes(str2):
        if sum_dashes(str1) == 0:
            check = True
        else:
            for i in str1:
                if i == "-":
                    if str2[str1.index(i)] == "-":
                        check = True
                    else:
                        break
    return check
    # error: can't read an alignment yet
    
def sum_dashes(str):
    count = 0
    for i in str:
        if i == "-":
            count = count + 1
    return count

if __name__=="__main__":
    str1 = input("String 1: ")
    str2 = input("String 2: ")
    print("same dashes? " + str(same_dashes(str1, str2)))