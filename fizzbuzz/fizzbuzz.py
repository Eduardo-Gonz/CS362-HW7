def fizzbuzz():
    result = []
    for i in range(1, 101):
        if(i % 3 == 0 and i % 5 == 0):
            print("FizzBuzz")
            result.append("FizzBuzz")
        elif(i % 3 == 0):
            print("Fizz")
            result.append("Fizz")
        elif(i % 5 == 0):
            print("Buzz")
            result.append("Buzz")
        else:
            print(i)
            result.append(i)
    

    return result