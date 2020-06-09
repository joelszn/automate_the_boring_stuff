def div_42_by(divide_by):
    try:
        return 42 / divide_by
    except ZeroDivisionError:
        print('Error: You tried to divide by Zero')

print(div_42_by(2))
print(div_42_by(12))
print(div_42_by(0))
print(div_42_by(1))


# ANOTHER EXAMPLE
numCats = -1
while int(numCats) < 0:
    print('how many cats do you have?')
    numCats = input()
    if int(numCats) > 0:
        try:
            if int(numCats) >=4:
                print('thats a lot of cats')
            else:
                print('not that many cats')
        except ValueError:
            print("You didn't enter a Number")
    else:
        print('Please enter a number greater than 0')