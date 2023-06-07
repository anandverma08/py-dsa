def check_paloindrome(s):
    s = s.replace(" ","")
    s = s.lower()
    l = len(s)
    res = {}
    for i in range(l):
        if s[i] in res:
            res[s[i]]+=1
        else:
            res[s[i]] = 1

    offsFound = 0

    for k in res:
        if l%2==0:
            if res[k]%2!=0:
                return False
        else:
            if res[k]%2!=0:
                offsFound+=1

    if offsFound==0 or offsFound>1:
        return False
    return True

print(check_paloindrome("Taco Coa"))