# Leetcode 70: Climbing Stairs
## Read description at https://leetcode.com/problems/climbing-stairs/description/?envType=study-plan-v2&envId=top-interview-150

### Top-Down Dynamic Programming
cache = dict() #Save responses here to avoid repetitive executions
def climbStairs(n: int) -> int:
    ## Base cases
    if n == 1:
        return 1
    if n == 2:
        return 2
    
    ## Return if solution is in cache
    if n in cache.keys():
        return cache[n]
    
    ## Recursive solution
    cache[n] = climbStairs(n-1) + climbStairs(n-2)
    return cache[n]


print (climbStairs(20))