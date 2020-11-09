for i in range(1,101):
    print((i if i % 5 else "Buzz") if i % 3 else ("Fizz" if i % 5 else "FizzBuzz"))
