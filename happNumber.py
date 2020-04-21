def isHappy( n):
    slow = n 
    fast = n 
    while(True): 
        slow = sumOfSquares(slow)
        fast = sumOfSquares(sumOfSquares(fast))
        if(slow != fast): 
            continue 
        else: 
            break
    return (slow == 1)
        
def sumOfSquares(n):
    squareSum = 0
    while(n): 
        squareSum += (n % 10) * (n % 10)
        n = int(n / 10)
    return squareSum


n = 7
if (isHappy(n)):
    print(n , "is a Happy number")
else: 
    print(n , "is not a Happy number") 
  