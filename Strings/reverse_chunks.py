def reverse_chunks(s, k):
    reversed = ""
    i = 0
    while i < len(s):
        if i+k <= len(s):
            j = k + i
            while j > i:
                reversed = "".join([reversed, s[j-1]])
                j = j-1
        else:
            while i < len(s):
                reversed = "".join([reversed, s[i]])
                i = i+1
        i = i+k
    return reversed

if __name__=="__main__":
    s = input("input string: ")
    k = int(input("reverse order: "))
    print(reverse_chunks(s, k))