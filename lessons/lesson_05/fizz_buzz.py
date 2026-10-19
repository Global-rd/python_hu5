#if number is divisible by 3 and 5: Fizzbuzz
#if number is divisible by only 3: Fizz
#if number is divisible by only 5: Buzz
#else: n



n = 15

if n % 3 == 0 and n % 5 == 0:
    print("FizzBuzz")
elif n % 3 == 0:
    print("Fizz")
elif n % 5 == 0:
    print("Buzz")
else:
    print(n)


#bad example:

if n % 3 == 0:
    print("Fizz")
elif n % 3 == 0 and n % 5 == 0:
    print("FizzBuzz")
elif n % 5 == 0:
    print("Buzz")
else:
    print(n)