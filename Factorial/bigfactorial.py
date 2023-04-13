def factorial(n):
    res = [None]*500
    res[0] = 1
    res_size = 1
    if n == 1:
        return 1
    x = 2
    while x <= n:
        res_size =  multiply(x, res, res_size)
        x = x+1

    k = res_size - 1
    ans = ""
    while k>=0:

        ans = ans + str(res[k])
        k = k-1
    print(ans)

def multiply(x,res,res_size):
    carry = 0
    i = 0
    while i < res_size:
        prod = res[i]*x + carry
        res[i] = prod % 10
        carry = prod//10
        i+=1

    while carry:
        res[res_size] = carry %10
        carry = carry//10
        res_size+=1

    return res_size

factorial(100)