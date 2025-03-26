
def febo(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else: 
        result = febo(n-1) + febo(n-2)
        print(f"Fibo({n}) = {result}")  # Print each computed Fibonacci number
        return result

# Example
print("Final Fibonacci Number:", febo(9))
