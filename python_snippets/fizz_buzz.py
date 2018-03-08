def fizz_buzz(numbers):
    for number in range(numbers):
        fizz = number % 2 == 0
        buzz = number % 5 == 0

        if fizz and buzz:
            print('fizzbuzz')
        elif fizz:
            print('fizz')
        elif buzz:
            print('buzz')
        else:
            print(number)


fizz_buzz(25)
