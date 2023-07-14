def climbStairs(n: int) -> int:
    if n == 1:
        return 1
    elif n == 2:
        return 2
    else:
        return climbStairs(n - 1) + climbStairs(n - 2)

print(climbStairs(4))