def divisible_by_three(x):
    return x % 3 == 0

def divisible_by_five(x):
    return x % 5 == 0


for x in range(1, 101):
    if divisible_by_three(x) & divisible_by_five(x):
        print("FizzBuzz")
    elif divisible_by_three(x):
        print("Fizz")
    elif divisible_by_five(x):
        print("Buzz")
    else:
        print(x)