def uniquechar(s):
    res = {}

    for i in range(len(s)):
        if s[i] in res:
            return False
        else:
            res[s[i]] = 1
    print(res)
    return True

print(uniquechar("ana"))