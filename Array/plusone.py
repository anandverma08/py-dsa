def plusOne(digits):
    sum = 0
    k = 1
    for i in range(len(digits)-1, -1, -1):
        sum = sum + k*digits[i]
        k=k*10
    sum+=1
    res = []
    s = str(sum)
    for i in range(len(s)):
        res.append(s[i])
    print(res)
plusOne([1,2,3,4])