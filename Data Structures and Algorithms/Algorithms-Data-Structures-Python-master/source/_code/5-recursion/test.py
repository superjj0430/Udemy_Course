# n! = 1*2*3........(n-1)*

# n* (n-1) * (n-2)...........2*1!

# def test(n):
#     result = 1
#     for item in range(1, n+1):
#         result = result * item
#     return result


def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)


print(test(3))
