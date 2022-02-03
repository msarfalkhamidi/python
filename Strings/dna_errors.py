def dna_errors(stra, strb):
    stra = stra.lower()
    strb = strb.lower()
    if len(stra) > len(strb):
        str = stra
        stra = strb
        strb = str
    error = 0
    for i in range(len(stra)):
        if stra[i] == "A" :
            error = error + 1
            # still not done yet

if __name__=="__main__":
    print("errors:", dna_errors(input("input dna a: "), input("input dna b: ")))