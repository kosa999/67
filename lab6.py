from functools import reduce
import operator

numbers = [2, 3, 4]
result = reduce(operator.mul, numbers)
print("otvet:", result)




def count_case(s):
    upper = sum(1 for c in s if c.isupper())
    lower = sum(1 for c in s if c.islower())
    print("Uppercase:", upper)
    print("Lowercase:", lower)

count_case("Hello KBTU!")




def is_palindrome(s):
    return s == s[::-1]

print(is_palindrome("radar"))  # True
print(is_palindrome("doner"))  # False




import time
import math

def delayed_sqrt(number, delay_ms):
    time.sleep(delay_ms / 1000)
    result = math.sqrt(number)
    print(f"Square root of {number} after {delay_ms} miliseconds is {result}")

delayed_sqrt(25100, 2123)





t = (True, 1, "yes")
print(all(t))  # True

t2 = (True, 0, "yes")
print(all(t2))  # False