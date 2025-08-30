def stringZigZag(string):
    string2 = ""
    strig_len = len(string)
    for i in range(strig_len // 2 + 1):
        print(i)
        if i == strig_len // 2 :
            string2 += string[i]
        else: 
            string2 += string[i] + string[strig_len - i - 1]
        # if i == strig_len // 2:
        #     string2 += string[i]
    print(string2)

string = "abcde"

stringZigZag(string)
